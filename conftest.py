import platform
from pathlib import Path
from slugify import slugify

import allure
import pytest
from playwright.sync_api import Browser, Page

from playwright_pytest.env_configurator import EnvConfigurator
from playwright_pytest.utils import set_allure_env_variable


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        default='dev',
        choices=['dev', 'test', 'stage', 'prod'],
        help="""
        Specify test environment for further utilization in test. Available options:
         * dev (default)
         * test
         * stage
         * prod
         """,
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(call, item):  # noqa: ARG001
    result = yield

    page: Page = item.funcargs['page']
    result = result.get_result()
    if result.failed and page:
        # Attach traceback
        page.context.tracing.stop(path='ma_trace.zip')
        path2trace = Path('ma_trace.zip')
        allure.attach.file(path2trace.absolute(), name=f'{slugify(item.nodeid)}-trace.zip', extension='zip')
        path2trace.unlink()

        # Attach screenshot
        allure.attach(
            page.screenshot(type='png'), name=f'{slugify(item.nodeid)}.png', attachment_type=allure.attachment_type.PNG
        )


@pytest.fixture(scope='session')
@allure.title('Configure browser')
def browser_context_args(browser_context_args):
    return {**browser_context_args, 'viewport': {'width': 1920, 'height': 1080}}


@allure.title('Process env configs.')
@pytest.fixture(scope='session', autouse=True)
def configurator(request: pytest.FixtureRequest) -> EnvConfigurator:
    # Process env data once. All other EnvConfigurator() calls will return the same instance.
    return EnvConfigurator(request.config.getoption('--env'))


@allure.title('Launch webdriver')
@pytest.fixture(scope='session', autouse=True)
def _set_allure_env_variables(browser: Browser, configurator: EnvConfigurator, request: pytest.FixtureRequest) -> None:
    set_allure_env_variable(request.config, 'DRIVER', browser.browser_type.name)
    set_allure_env_variable(request.config, 'BROWSER_VERSION', browser.version)
    set_allure_env_variable(request.config, 'OS', platform.platform())
    set_allure_env_variable(request.config, 'OS_VERSION', platform.release())
    set_allure_env_variable(request.config, 'ENVIRONMENT', configurator.env)
    # add_pytest_res_evn_file(request.config, 'BROWSER_RESOLUTION', selenium.get_window_size())


@pytest.fixture()
def page(page: Page) -> Page:
    """Start custom traceback recording."""
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page  # noqa: PT022
