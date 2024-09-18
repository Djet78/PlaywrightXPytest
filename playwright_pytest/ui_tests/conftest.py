import allure
import pytest

from pathlib import Path
from slugify import slugify
from playwright.sync_api import Browser, Page


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


@pytest.fixture()
def page(page: Page) -> Page:
    """Start custom traceback recording."""
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page  # noqa: PT022


@pytest.fixture(autouse=True)
def _set_driver_allure_tag(browser: Browser) -> None:
    allure.dynamic.epic(f'{browser.browser_type.name} {browser.version}')
