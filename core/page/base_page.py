from playwright.sync_api import Page, Locator
from core.types import Button, LoadState, ModifierActions, StateOfElement, WaitUntil
import requests

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.context = page.context

    def goto(self, url: str, options: dict = None):
        self.page.goto(url, **(options or {}))

    def go_forward(self, options: dict = None):
        self.page.go_forward(**(options or {}))

    def go_back(self, options: dict = None):
        self.page.go_back(**(options or {}))

    def reload(self, options: dict = None):
        self.page.reload(**(options or {}))

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def screenshot(self, options: dict = None) -> bytes:
        return self.page.screenshot(**(options or {}))

    def check(self, locator: Locator, options: dict = None):
        locator.check(**(options or {}))

    def clear(self, locator: Locator, options: dict = None):
        locator.clear(**(options or {}))

    def click(self, locator: Locator, index: int = None, options: dict = None):
        if index is not None:
            locator.nth(index).click(**(options or {}))
        else:
            locator.click(**(options or {}))

    def dblclick(self, locator: Locator, index: int = None, options: dict = None):
        if index is not None:
            locator.nth(index).dblclick(**(options or {}))
        else:
            locator.dblclick(**(options or {}))

    def drag_to(self, source: Locator, target: Locator, options: dict = None):
        source.drag_to(target, **(options or {}))

    def fill(self, locator: Locator, value: str, options: dict = None):
        locator.fill(value, **(options or {}))

    def focus(self, locator: Locator, options: dict = None):
        locator.focus(**(options or {}))

    def hover(self, locator: Locator, options: dict = None):
        locator.hover(**(options or {}))

    def get_inner_html(self, locator: Locator, options: dict = None) -> str:
        return locator.inner_html(**(options or {}))

    def uncheck(self, locator: Locator, options: dict = None):
        locator.uncheck(**(options or {}))

    def press(self, locator: Locator, key: str, options: dict = None):
        locator.press(key, **(options or {}))

    def wait_for_page_load(self, state: LoadState = None, options: dict = None):
        self.page.wait_for_load_state(state, **(options or {}))
        return self

    def wait_for_element(self, locator: Locator, options: dict = None):
        locator.wait_for(**(options or {}))

    def wait_for_element_to_be_visible(self, locator: Locator):
        self.wait_for_element(locator, {"state": "visible"})

    def wait_for_element_to_be_hidden(self, locator: Locator):
        self.wait_for_element(locator, {"state": "hidden"})
