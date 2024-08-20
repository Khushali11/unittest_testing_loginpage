import unittest
import pytest
import time
import allure


# LoginPage class we are testing
class Loginpage():
    def __init__(self, valid_username, valid_password):
        self.valid_username = valid_username
        self.valid_password = valid_password

    def login(self, username: object, password: object) -> object:
        if username == self.valid_username and password == self.valid_password:
            return "Login successful"
        else:
            return "Invalid credentials"

    def validate_username(self, username):
        if len(username) < 3:
            return "Username too short"
        elif len(username) > 20:
            return "Username too long"
        else:
            return "Username valid"

    def validate_password(self, password):
        if len(password) < 6:
            return "Password too short"
        else:
            return "Password valid"


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        """Set up a LoginPage instance with known valid credentials."""
        self.login_page = Loginpage("validuser", "validpassword")

    @allure.epic("Test Login sucessful")
    @allure.feature("TC#0 Test login with valid credentials")
    def test_login_sucessful(self):
        """Test login with valid credentials."""
        result = self.login_page.login("validuser", "validpassword")
        self.assertEqual(result, "Login successful")

    @allure.epic("Invalid credentials")
    @allure.feature("TC#1 Test login with invalid username and valid password credentials")
    def test_login_invalid_username(self):
        """Test login with invalid username and valid password credentials."""
        result = self.login_page.login("invaliduser", "validpassword")
        self.assertEqual(result, "Invalid credentials")

    @allure.epic("Invalid credentials")
    @allure.feature("TC#2 Test login with valid username and invalid password credentials")
    def test_login_invalid_password(self):
        """Test login with an invalid password."""
        result = self.login_page.login("validuser", "invalidpassword")
        self.assertEqual(result, "Invalid credentials")

    @allure.epic("Invalid credentials")
    @allure.feature("TC#3 Test login with invalid username and invalid password credentials")
    def test_login_invalid_both(self):
        """Test login with both username and password invalid."""
        result = self.login_page.login("invaliduser", "invalidpassword")
        self.assertEqual(result, "Invalid credentials")

    @allure.epic("Username too short")
    @allure.feature("TC#4 Test username validation for too short usernames.")
    def test_validate_username_too_short(self):
        """Test username validation for too short usernames."""
        result = self.login_page.validate_username("ab")
        self.assertEqual(result, "Username too short")

    @allure.epic("Username too long")
    @allure.feature("TC#5 Test username validation for too long usernames.")
    def test_validate_username_too_long(self):
        """Test username validation for too long usernames."""
        result = self.login_page.validate_username("a" * 21)
        self.assertEqual(result, "Username too long")

    @allure.epic("Username valid")
    @allure.feature("TC#6 Test username validation for valid usernames.")
    def test_validate_username_valid(self):
        """Test username validation for valid usernames."""
        result = self.login_page.validate_username("validuser")
        self.assertEqual(result, "Username valid")

    @allure.epic("Password too short")
    @allure.feature("TC#7 Test password validation for too short passwords.")
    def test_validate_password_too_short(self):
        """Test password validation for too short passwords."""
        result = self.login_page.validate_password("short")
        self.assertEqual(result, "Password too short")

    @allure.epic("Password valid")
    @allure.feature("TC#8 Test password validation for valid passwords.")
    def test_validate_password_valid(self):
        """Test password validation for valid passwords."""
        result = self.login_page.validate_password("validpassword")
        self.assertEqual(result, "Password valid")


if __name__ == '__main__':
    unittest.main()
