import pytest
from lib.password_checker import *

def test_if_password_is_correct():
    password_checker = PasswordChecker()
    assert password_checker.check('password123') == True

def test_error_if_password_is_invalid():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('Nope')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."