import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    def test_substraction(self):
        self.asserEqual(self.calc.substract(6,1),5)
        self.assertEqual(self.calc.substract(99,90),9)
    def test_multiplicaiton(self):
        self.assertEqual(self.calc.multiply(10,0),0)
        self.assertEqual(self.calc.multiply(5,6),30)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,0),None)
        self.assertEqual(self.calc.divide(100,10),10)

if __name__=='__main__':
    unittest.main()
