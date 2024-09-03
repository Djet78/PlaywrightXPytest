import allure
import pytest


@pytest.fixture(scope='session')
@allure.title('Configure browser')
def browser_context_args(browser_context_args):
    return {**browser_context_args, 'viewport': {'width': 1920, 'height': 1080}}
