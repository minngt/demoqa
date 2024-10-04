import pytest
from playwright.sync_api import expect

from data.login_credential import username, password
from pages.login_page import LoginPage
from constants.ui_text import UIText
from fixtures.page_fixture import login_page

@pytest.mark.usefixtures('login_page')
class TestLoginPage:

    def test_login_with_valid_credentials(self, page):
        login_page = LoginPage(page)
        login_page.login({'userName': username, 'password': password})
        expect(page).to_have_url('https://demoqa.com/profile')

    def test_login_with_invalid_credentials(self, page):
        login_page = LoginPage(page)
        login_page.login({'userName': 'invalid', 'password': 'wrongpassword'})
        assert login_page.error_message.text_content() == UIText.LOGIN_ERROR
