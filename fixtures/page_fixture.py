import pytest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.book_page import BookPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)