import pytest


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {**browser_context_args, 'viewport': {'width': 1920, 'height': 1080}}


# # Set the global timeout
# from playwright.sync_api import expect
#
# expect.set_options(timeout=10_000)
