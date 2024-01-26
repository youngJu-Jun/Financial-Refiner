import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
def random_time() -> float:
    return random.uniform(0.5, 1)
def oil_crawler(driver) -> list:
    # user setting
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    options = Options()
    options.add_experimental_option("detatch", True)
    options.add_argument("--disable-blink-features=AutomationControlled") #강제로 자동화 브라우저가 아님을 말함
    driver.implicitly_wait(10)

    driver.get("https://www.financialjuice.com/home") #사이트 접속
    driver.maximize_window()
    
    # click login button
    li = driver.find_element(By.ID, 'liSignIn') # Sign in 버튼을 포함하는 li 태그 찾기
    li.find_element(By.TAG_NAME, "a").click() # li 태그 안에 있는 a 태그 선택
    # input userID & PWD
    inputEmail = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_inputEmail")
    time.sleep(random_time())
    inputPWD = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_inputPassword")
    time.sleep(random_time())
    inputEmail.send_keys("jhnamugeona@gmail.com")
    inputPWD.send_keys("sangmoon123")
    time.sleep(random_time())
    loginButton = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_btnLogin") #버튼인데 input 태그로 되어 있음
    loginButton.click()
    time.sleep(random_time())
    
    # move to Commodities tab
    # no class at commodities button -> use xpath
    headlineTitle = driver.find_elements(By.CLASS_NAME, "headline-title")
    result = []
    for e in headlineTitle:
        result.append(e.text)
    # for e in headlineTitle2:
    #     result.append(e.text)
    return result