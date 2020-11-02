"""
Unit tests for the calculator library
"""

import calculator_functions


class TestCalculator:

    def test_addition(self):
        assert 10 == calculator_functions.addition(5, 5)
