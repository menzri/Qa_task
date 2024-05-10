import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from model import select_element, send_text, is_element_visible
from config import generate_random

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()
@pytest.mark.parametrize("username, password", [("user1", "password1"),("user2", "password2"),("user3", "password3")])
def test_login_success(chrome_browser, username, password):
    login(chrome_browser, username, password)
    welcome_message = f"//p[contains(text(), 'Welcome, {username}! This is your profile.')]"
    is_element_visible(chrome_browser, welcome_message)

def test_login_invalid_credentials(chrome_browser):
    invalidusername = generate_random()
    invalidpassword = generate_random()
    login(chrome_browser, invalidusername, invalidpassword)
    error_message = "//p[contains(text(), 'Invalid username or password.')]"
    is_element_visible(chrome_browser, error_message)

def test_login_empty_input(chrome_browser):
    login(chrome_browser, "", "")
    error_message = "//p[contains(text(), 'Invalid username or password.')]"
    is_element_visible(chrome_browser, error_message)

def login(driver, username, password):
    driver.get("https://logintest.kartywallet.app/login")
    send_text(driver, "//input[@id='username']", username)
    send_text(driver, "//input[@id='password']", password)
    select_element(driver, "//button[@class='btn btn-primary' and text()='Login']")