import pytest
from playwright.sync_api import sync_playwright, Browser, Page


@pytest.fixture(scope="function")
def browser() -> Browser:
    # Создаем экземпляр Playwright самостоятельно
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()  # Важно остановить Playwright


@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
