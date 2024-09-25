import pytest
from playwright.sync_api import sync_playwright

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser

        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(storage_state='storageState.json')  # Restore session state
    page = context.new_page()

    page.goto("https://demoqa.com/login")
    yield page
    context.close()


