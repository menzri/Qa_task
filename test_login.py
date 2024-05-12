import pytest
from model import select_element, send_text, is_element_visible
from config import generate_random

# Test case to verify successful login with valid credentials
@pytest.mark.parametrize("username, password", [("user1", "password1"),("user2", "password2"),("user3", "password3")])
def test_login_success(chrome_browser, username, password):
    login(chrome_browser, username, password)
    welcome_message = f"//p[contains(text(), 'Welcome, {username}! This is your profile.')]"
    is_element_visible(chrome_browser, welcome_message)
# Test case to verify error message for invalid credentials
def test_login_invalid_credentials(chrome_browser):
    invalidusername = generate_random()
    invalidpassword = generate_random()
    login(chrome_browser, invalidusername, invalidpassword)
    error_message = "//p[contains(text(), 'Invalid username or password.')]"
    is_element_visible(chrome_browser, error_message)
# Test case to verify error message for empty input fields
def test_login_empty_input(chrome_browser):
    login(chrome_browser, "", "")
    error_message = "//p[contains(text(), 'Invalid username or password.')]"
    is_element_visible(chrome_browser, error_message)
# Function to perform login action
def login(driver, username, password):
    driver.get("https://logintest.kartywallet.app/login")
    send_text(driver, "//input[@id='username']", username)
    send_text(driver, "//input[@id='password']", password)
    select_element(driver, "//button[@class='btn btn-primary' and text()='Login']")