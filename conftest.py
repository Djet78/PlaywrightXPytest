import platform
from slugify import slugify

import allure
import pytest
from playwright.sync_api import Page

from playwright_pytest.env_configurator import EnvConfigurator
from playwright_pytest.utils import add_pytest_res_evn_file


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


# TODO update for playwright
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(call, item):  # noqa: ARG001
    # Get screenshot of a failed test
    result = yield
    result = result.get_result()
    page: Page = item.funcargs['page']
    if result.failed and page:
        allure.attach(
            page.screenshot(type='png'), name=f'{slugify(item.nodeid)}.png', attachment_type=allure.attachment_type.PNG
        )


@pytest.fixture(scope='session')
@allure.title('Configure browser')
def browser_context_args(browser_context_args):
    return {**browser_context_args, 'viewport': {'width': 1920, 'height': 1080}}


@allure.title('Process env configs.')
@pytest.fixture(scope='session', autouse=True)
def configurator(request):
    # Process env data once. All other EnvConfigurator() calls will return the same instance.
    return EnvConfigurator(request.config.getoption('--env'))


@allure.title('Launch webdriver')
@pytest.fixture(scope='session')
def browser(browser, configurator, request):
    add_pytest_res_evn_file(request.config, 'DRIVER', browser.browser_type.name)
    add_pytest_res_evn_file(request.config, 'BROWSER_VERSION', browser.version)
    add_pytest_res_evn_file(request.config, 'OS', platform.platform())
    add_pytest_res_evn_file(request.config, 'OS_VERSION', platform.release())
    add_pytest_res_evn_file(request.config, 'ENVIRONMENT', configurator.env)
    # add_pytest_res_evn_file(request.config, 'BROWSER_RESOLUTION', selenium.get_window_size())
    return browser
