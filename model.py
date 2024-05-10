from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIMER = 20
def select_element(chrome_browser, ELEMENT):
    try:
        element_selection = WebDriverWait(chrome_browser, WAIT_TIMER).until(EC.visibility_of_element_located((By.XPATH, ELEMENT)))
        assert element_selection.is_displayed(), f"Element with XPath '{ELEMENT}' is not visible."
        element_selection.click()
    except AssertionError as e:
        raise e
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise AssertionError(f"Element  with XPath '{ELEMENT}' is not visible.")
    
def send_text(chrome_browser, INPUTID, text):
    try:
        input = WebDriverWait(chrome_browser, WAIT_TIMER).until(EC.visibility_of_element_located((By.XPATH, INPUTID)))
        assert input.is_displayed(), f"Element with XPath '{INPUTID}' is not visible."
        input.send_keys(text) 
    except AssertionError as e:
        raise e
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise AssertionError(f"Element with XPath '{INPUTID}' is not visible.")
    
def is_element_visible(chrome_browser, element_id):
    try:
        element = WebDriverWait(chrome_browser, WAIT_TIMER).until(
            EC.visibility_of_element_located((By.XPATH, element_id))
        )
        assert element.is_displayed(), f"Element  with XPath '{element_id}' is not visible."
    except AssertionError as e:
        raise e
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise AssertionError(f"Element  with XPath '{element_id}' is not visible.")
    