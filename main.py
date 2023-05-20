from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

if __name__ == '__main__':
    print('开始抓取')

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://www.douyin.com/")
    els = driver.find_elements(By.TAG_NAME, 'button')


    def findLoginButton(bt: WebElement):
        if bt.text == '登录':
            return True
        return False


    loginButton: WebElement = list(filter(findLoginButton, els))[0]
    print(loginButton.text)

    while True:
        login_status = driver.get_cookie("LOGIN_STATUS")
        if login_status and login_status['value'] == '1':
            break

    navigation: WebElement = WebDriverWait(driver, 120).until(lambda x: x.find_element(By.CSS_SELECTOR, 'div[data-e2e=\'douyin-navigation\']'))
    pass

    driver.quit()
    print('抓取结束')
