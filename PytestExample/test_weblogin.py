from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.delete_all_cookies()
    driver.implicitly_wait(10)

def teardown_module(module):
    driver.quit()

def test_google():
    driver.get('https://www.google.co.uk/')
    assert driver.title == "Google"

def test_google_url():
    driver.get('https://www.google.co.uk/')
    assert driver.current_url == "https://www.google.co.uk/"

def test_facebook():
    driver.get('https://www.facebook.com/')
    assert driver.title == "Facebook – log in or sign up"

def test_gmail():
    driver.get('https://mail.google.com/')
    assert driver.title == "Gmail"
