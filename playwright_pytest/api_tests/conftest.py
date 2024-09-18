import allure
import pytest

from typing import Generator

from playwright.sync_api import Playwright, APIRequestContext
from playwright_pytest.components.env_configurator import EnvConfigurator


@pytest.fixture(scope='session')
def api_request(playwright: Playwright, configurator: EnvConfigurator) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url=configurator.booking_endp)
    yield request_context
    request_context.dispose()


@pytest.fixture(autouse=True)
def _set_driver_allure_tag() -> None:
    allure.dynamic.epic('API')
