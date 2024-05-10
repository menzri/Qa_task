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
    
@pytest.mark.parametrize("username, email", [("user1", "user1@example.com"), ("user2", "user2@example.com"), ("user3", "user3@example.com")])
def test_reset_success(chrome_browser, username, email):
    reset_password(chrome_browser, username)
    email_success = f"//p[contains(text(), 'A password reset link has been sent to {email}.')]"
    is_element_visible(chrome_browser, email_success)

def test_invalid(chrome_browser):
    username = generate_random()
    reset_password(chrome_browser, username)
    invalid_email = f"//p[contains(text(), 'User name not found {username}.')]"
    is_element_visible(chrome_browser, invalid_email)

def test_empty(chrome_browser):
    reset_password(chrome_browser, "")
    empty_user = "//p[contains(text(), 'User name not found .')]"
    is_element_visible(chrome_browser, empty_user)

def reset_password(chrome_browser, username_input):
    chrome_browser.get("https://logintest.kartywallet.app/login")
    reset_xpath = "//p[@class='mt-3 mb-0']/a[text()='Reset it']"
    select_element(chrome_browser, reset_xpath)
    username_xpath = "//input[@id='username']"
    send_text(chrome_browser, username_xpath, username_input)
    reset_button = "//button[@type='submit' and text()='Reset Password']"
    select_element(chrome_browser, reset_button)