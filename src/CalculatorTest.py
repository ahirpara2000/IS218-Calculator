import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_result_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)

    def test_multiplication_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(3, 2), 6)

    def test_division_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(3, 2), 1.5)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(3), 9)


if __name__ == '__main__':
    unittest.main()
