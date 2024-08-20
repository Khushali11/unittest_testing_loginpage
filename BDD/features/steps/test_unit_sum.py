import unittest
import allure
import pytest


def add(a, b):
    return a + b


class TestAddFunction(unittest.TestCase):
    @allure.epic("Test addition function")
    @allure.feature("TC#0 ADD POSITIVE NUMBER")
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    @allure.epic("Test addition function")
    @allure.feature("TC#1 ADD NEGATIVE NUMBER")
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    @allure.epic("Test addition function")
    @allure.feature("TC#2 ADD mixed NUMBER")
    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)


if __name__ == '__main__':
    unittest.main()
