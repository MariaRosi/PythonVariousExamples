import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("init_driver")
class TestBase:
    pass


class TestHubSpot(TestBase):
    @pytest.mark.parametrize("user, pwd", [("admin@example.com", "admin"), ("admin1@example.com", "admin123")])
    def test_hubspot_login(self,user,pwd):
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, 'username').send_keys(user)
        self.driver.find_element(By.ID, 'password').send_keys(pwd)