import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance befor each test"""
        self.calcul = SimpleCalculator()

    def test_addition(self):
        """Test teh add methode"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtract methode"""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-8, 3), -11)
        self.assertEqual(self.calc.subtract(8, -3), 11)
        self.assertEqual(self.calc.subtract(-8, -3), -5)

    def test_multiplication(self):
        """Test the multiplication methode"""
        self.assertEqual(self.calc.multiply(10, 3), 30)
        self.assertEqual(self.calc.multiply(-8, 3), -24)
        self.assertEqual(self.calc.multiply(8, -3), -24)
        self.assertEqual(self.calc.multiply(-8, -3), 24)
    
    def test_division(self):
        """Test the division  methode"""
        self.assertEqual(self.calc.divide(10, 3), 10/3)
        self.assertEqual(self.calc.divide(-8, 3), -8/3)
        self.assertEqual(self.calc.divide(8, -3), -8/3)
        self.assertEqual(self.calc.divide(-8, -3), 8/3)
        # Divide by zero
        self.assertEqual(self.calc.divide(-8, 0), "ZeroDivisionError")
