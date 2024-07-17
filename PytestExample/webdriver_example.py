from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Maria\\PythonProject\\driver\chromedriver.exe")
driver.get('https://www.example.com')
print(driver.title)
