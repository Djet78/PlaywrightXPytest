import platform

import allure
import pytest

from playwright_pytest.components.env_configurator import EnvConfigurator
from playwright_pytest.components.utils import set_allure_env_variable


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


@allure.title('Process env configs.')
@pytest.fixture(scope='session', autouse=True)
def configurator(request: pytest.FixtureRequest) -> EnvConfigurator:
    # Process env data once. All other EnvConfigurator() calls will return the same instance.
    return EnvConfigurator(request.config.getoption('--env'))


@allure.title('Launch webdriver')
@pytest.fixture(scope='session', autouse=True)
def _set_allure_env_variables(configurator: EnvConfigurator, request: pytest.FixtureRequest) -> None:
    set_allure_env_variable(request.config, 'OS', platform.platform())
    set_allure_env_variable(request.config, 'OS_VERSION', platform.release())
    set_allure_env_variable(request.config, 'ENVIRONMENT', configurator.env)
    # add_pytest_res_evn_file(request.config, 'BROWSER_RESOLUTION', selenium.get_window_size())
