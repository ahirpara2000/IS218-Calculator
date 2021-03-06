import unittest
from calculator.Calculator import Calculator
from CSVReader.CSVreader import ReadCsv


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    # 1. Check calculator instance
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # 2. Check result property
    def test_result_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    # 3. Check addition method
    def test_add_method_calculator(self):
        csv_data = ReadCsv("../tests/Data/Unit Test Addition.csv").data

        for val in csv_data:
            val1 = int(val['Value 1'])
            val2 = int(val['Value 2'])
            result = int(val['Result'])

            self.assertEqual(self.calculator.add(val1, val2), result)

        del csv_data

    # 4. Check subtraction method
    def test_subtract_method_calculator(self):
        csv_data = ReadCsv("../tests/Data/Unit Test Subtraction.csv").data

        for val in csv_data:
            val1 = int(val['Value 1'])
            val2 = int(val['Value 2'])
            result = int(val['Result'])

            self.assertEqual(self.calculator.subtract(val2, val1), result)

    # 5. Check multiplication method
    def test_multiplication_method_calculator(self):
        csv_data = ReadCsv("../tests/Data/Unit Test Multiplication.csv").data

        for val in csv_data:
            val1 = int(val['Value 1'])
            val2 = int(val['Value 2'])
            result = int(val['Result'])

            self.assertEqual(self.calculator.multiply(val1, val2), result)

    # 6. Check division method
    def test_division_method_calculator(self):
        csv_data = ReadCsv("../tests/Data/Unit Test Division.csv").data

        for val in csv_data:
            val1 = float(val['Value 1'])
            val2 = float(val['Value 2'])
            result = float(val['Result'])

            self.assertEqual(self.calculator.divide(val2, val1), result)

    # 7. Check division method with 0
    def test_division_method_by_zero_calculator(self):
        calculator = self.calculator
        self.assertEqual(self.calculator.divide(10, 0), "Error: Cannot be divided by 0.")

    # 8. Check square method
    def test_square_method_calculator(self):
        csv_data = ReadCsv("../tests/Data/Unit Test Square.csv").data

        for val in csv_data:
            val1 = float(val['Value 1'])
            result = float(val['Result'])

            self.assertEqual(self.calculator.square(val1), result)

    # 9. Check square root method
    def test_square_root_method_calculator(self):
        csv_data = ReadCsv("../tests/Data/Unit Test Square Root.csv").data

        for val in csv_data:
            val1 = float(val['Value 1'])
            result = float(val['Result'])

            self.assertEqual(self.calculator.square_root(val1), result)


if __name__ == '__main__':
    unittest.main()
