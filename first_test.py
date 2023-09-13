from app.calculator import Calculator
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_multiply_corect(self):
        assert self.calc.multiply(self, 2,2) == 4
    def test_division_corect(self):
        assert self.calc.division(self, 10,2) == 5
    def test_subtraction_corect(self):
        assert self.calc.subtraction(self, 10,2) == 8
    def test_adding_corect(self):
        assert self.calc.adding(self, 10,2) == 12