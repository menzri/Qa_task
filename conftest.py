import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Fixture to set up and tear down the WebDriver instance
@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()