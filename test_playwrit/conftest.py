# conftest.py
import pytest
from playwright.sync_api import Playwright, Browser
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def browser(playwright: Playwright) -> Browser:
    # Используем встроенную фикстуру playwright
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
