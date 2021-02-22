import unittest
from Calculator import Calculator
from CSVreader import ReadCsv


class MyTestCase(unittest.TestCase):

    # 1. Check calculator instance
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    # 2. Check result property
    def test_result_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    # 3. Check addition method
    def test_add_method_calculator(self):
        calculator = Calculator()

        csv_data = ReadCsv("//./src/Unit Test Addition.csv").data

        for val in csv_data:
            val1 = int(val['Value 1'])
            val2 = int(val['Value 2'])
            result = int(val['Result'])

            self.assertEqual(calculator.add(val1, val2), result)

        del csv_data

    # 4. Check subtraction method
    def test_subtract_method_calculator(self):
        csv_data = ReadCsv("//./src/Unit Test Subtraction.csv").data

        calculator = Calculator()
        for val in csv_data:
            val1 = int(val['Value 1'])
            val2 = int(val['Value 2'])
            result = int(val['Result'])

            self.assertEqual(calculator.subtract(val2, val1), result)

    # 5. Check multiplication method
    def test_multiplication_method_calculator(self):
        csv_data = ReadCsv("//./src/Unit Test Multiplication.csv").data

        calculator = Calculator()
        for val in csv_data:
            val1 = int(val['Value 1'])
            val2 = int(val['Value 2'])
            result = int(val['Result'])

            self.assertEqual(calculator.multiply(val1, val2), result)

    # 6. Check division method
    def test_division_method_calculator(self):
        csv_data = ReadCsv("//./src/Unit Test Division.csv").data

        calculator = Calculator()
        for val in csv_data:
            val1 = float(val['Value 1'])
            val2 = float(val['Value 2'])
            result = float(val['Result'])

            self.assertEqual(calculator.divide(val2, val1), result)

    # 7. Check square method
    def test_square_method_calculator(self):
        calculator = Calculator()

        csv_data = ReadCsv("//./src/Unit Test Square.csv").data

        calculator = Calculator()
        for val in csv_data:
            val1 = float(val['Value 1'])
            result = float(val['Result'])

            self.assertEqual(calculator.square(val1), result)

    # 8. Check square root method
    def test_square_root_method_calculator(self):
        calculator = Calculator()

        csv_data = ReadCsv("//./src/Unit Test Square Root.csv").data

        calculator = Calculator()
        for val in csv_data:
            val1 = float(val['Value 1'])
            result = float(val['Result'])

            self.assertEqual(calculator.square_root(val1), result)


if __name__ == '__main__':
    unittest.main()
