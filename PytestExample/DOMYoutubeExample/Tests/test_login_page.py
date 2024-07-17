from PytestExample.DOMYoutubeExample.Config.config import TestData
from PytestExample.DOMYoutubeExample.Pages.login_page import LoginPage
from PytestExample.DOMYoutubeExample.Tests.test_base import TestBase


class TestLogin(TestBase):

    def test_login_page_signup_link_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_signup_link_visible()
        assert flag

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_login_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)

