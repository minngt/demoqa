from core.page.base_page import BasePage
from pages.locators.login_locator import LoginLocator

class LoginPage(BasePage):

    @property
    def url(self):
        return self.page.goto('https://www.demoqa.com/login')

    @property
    def username_textbox(self):
        return self.page.locator(LoginLocator.USERNAME_TEXT_BOX)

    @property
    def password_textbox(self):
        return self.page.locator(LoginLocator.PASSWORD_TEXT_BOX)

    @property
    def login_button(self):
        return self.page.locator(LoginLocator.LOGIN_BUTTON)

    @property
    def error_message(self):
        return self.page.locator(LoginLocator.ERROR_MESSAGE_TEXT)

    def type_username(self, username: str):
        self.username_textbox.fill(username)

    def type_password(self, password: str):
        self.password_textbox.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, info: dict):
        self.type_username(info['userName'])
        self.type_password(info['password'])
        self.click_login_button()

