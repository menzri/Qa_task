# QA_Task

## Overview

This project implements functionalities related to User Login and Password Reset.

## Setup Instructions

### Prerequisites
- Python installed on your machine ([Download Python](https://www.python.org/downloads/))
- Pip package manager

### Installation
1. Install the `webdriver-manager` package: pip install webdriver-manager
2. Install pytest for running tests: pip install pytest
3. Install Selenium version 4.0.0: pip install selenium==4.0.0 
### Running Tests
- To run all tests: pytest -v
- To run tests in a specific file (replace `<file_name>` with the actual file name containing your tests): pytest -v file_name.py
  
## Use Cases

### Use Case 1: User Login
- Verify that user can login successfully.
- Verify that user is directed to the profile page after successful login.
- Verify that user sees an error message when entering invalid credentials.
- Verify that user sees an error message when leaving username and/or password fields blank.

### Use Case 2: Password Reset
- Verify that user receives an email with instructions on how to reset their password after entering valid username and clicking "Reset Password" (shows successful message).
- Verify that user sees an error message when entering invalid username.
- Verify that user sees an error message when leaving username field blank.
