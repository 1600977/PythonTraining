import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture()
def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return options

@pytest.fixture()
def driver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

@pytest.mark.skip('correct test')
def test_succefull_autotization(driver):
    driver.get('https://www.saucedemo.com/')   
    username = driver.find_element(By.XPATH,'//input[@data-test="username"]') 
    username.send_keys('standard_user')
    password = driver.find_element(By.XPATH,'//input[@data-test="password"]') 
    password.send_keys('secret_sauce')
    login = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login.click()
    sleep(5)
    products_title = driver.find_element(By.XPATH,'//span[@class="title"]') 
    assert products_title.text == 'Products'#helolo
    driver.close()

@pytest.mark.skip('no needed')
def test_wrong_password(driver):
    driver.get('https://www.saucedemo.com/')
    username = driver.find_element(By.XPATH,'//input[@data-test="username"]')
    username.send_keys('locked_out_user')
    password = driver.find_element(By.XPATH,'//input[@data-test="password"]')
    password.send_keys('secret_sauce')
    login = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login.click()
    error_title = driver.find_element(By.XPATH,'//h3[@data-test="error"]')
    assert error_title.text == 'Epic sadface: Sorry, this user has been locked out.'
    driver.close()

def test_empty_field(driver):
    driver.get('https://www.saucedemo.com/')
    login = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login.click()
    error = driver.find_element(By.XPATH,'//h3[@data-test="error"]')
    print(error.is_displayed())
    print(error.is_enabled())
    print(error.is_selected())
    print(error.tag_name)
    print(error.rect)
    print(error.value_of_css_property('margin-block-start'))
    print(error.text)
    assert error.text == 'Epic sadface: Username is required'



