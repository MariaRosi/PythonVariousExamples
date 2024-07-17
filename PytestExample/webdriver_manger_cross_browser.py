import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import selenium

print(selenium.__version__)

browser_name = "edge"
try:
    if browser_name == "chrome":
        print("chrome")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        print("firefox")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        print("edge")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.implicitly_wait(10)
    driver.get("https://app.hubspot.com/")

    driver.find_element(By.ID, 'username').send_keys('maria.rosi2008@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('test123')
    driver.find_element(By.ID, 'loginBtn').click()

    time.sleep(5)

    driver.quit()
except Exception as e:
    print(f"Error initializing WebDriver: {e}")



