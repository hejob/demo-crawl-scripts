# see [https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('./chromedriver/chromedriver')
# driver.get('https://www.python.org/')
# print(driver.title)

driver.get('https://www.bilibili.com/video/BV1c4411e77t/')
print(driver.title)
# driver.find_element_by_xpath('//h1')

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h1"))
    )
    print(element.text)
finally:
    driver.quit()
