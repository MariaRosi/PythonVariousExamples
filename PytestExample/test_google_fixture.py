from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    print("\n--------------setup-------------")
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.co.uk")

    yield
    print("\n--------------teardown-------------")
    driver.quit()

#def test_google_title(init_driver):
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"

#def test_google_url(init_driver):
@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.co.uk/"

