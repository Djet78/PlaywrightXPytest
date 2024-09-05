import platform

import allure
import pytest

from playwright_pytest.env_configurator import EnvConfigurator
from playwright_pytest.utils import add_pytest_res_evn_file


from allure_commons.types import AttachmentType


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption(
        '--driver',
        action='store',
        default='chrome',
        choices=['chrome', 'firefox', 'edge'],
        help="""
        Pytest will run tests against specified browser. Available options:
         -- chrome (default)
         -- firefox
         -- edge
         """,
    )
    parser.addoption(
        '--env',
        action='store',
        default='dev',
        choices=['dev', 'test', 'stage', 'prod'],
        help="""
        Specify test environment for further utilization in test. Available options:
         -- dev (default)
         -- test
         -- stage
         -- prod
         """,
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(call, item):  # noqa: ARG001
    # Get screenshot of a failed test
    result = yield
    result = result.get_result()
    driver = item.funcargs.get('selenium')
    if result.failed and driver:
        allure.attach(driver.get_screenshot_as_png(), 'UI Screenshot', attachment_type=AttachmentType.PNG)


@pytest.fixture(scope='session')
@allure.title('Configure browser')
def browser_context_args(browser_context_args):
    return {**browser_context_args, 'viewport': {'width': 1920, 'height': 1080}}


@allure.title('Process env configs.')
@pytest.fixture(scope='session', autouse=True)
def configurator(request):
    # Proccess env data once. All other EnvConfigurator() calls will return the same instance.
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
