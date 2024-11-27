import unittest
from Data.Lab1.Classes.Calculator import Calculator

class TestCalculator(unittest.TestCase):
    class TestCalculator(unittest.TestCase):

        def setUp(self):
            """Set up a calculator instance before each test."""
            self.calc = Calculator()

        def test_add_positive_numbers(self):
            """Test the addition of two positive numbers."""
            result = self.calc.add(10, 5)
            self.assertEqual(result, 15)

        def test_add_negative_numbers(self):
            """Test the addition of two negative numbers."""
            result = self.calc.add(-10, -5)
            self.assertEqual(result, -15)

        def test_add_positive_and_negative(self):
            """Test the addition of a positive and a negative number."""
            result = self.calc.add(10, -5)
            self.assertEqual(result, 5)

        def test_add_zero(self):
            """Test the addition when one of the operands is zero."""
            result = self.calc.add(10, 0)
            self.assertEqual(result, 10)

        def test_add_negative_to_zero(self):
            """Test the addition when one operand is negative and the other is zero."""
            result = self.calc.add(0, -5)
            self.assertEqual(result, -5)

        def test_add_non_number_input(self):
            """Test that an error is raised when a non-number input is provided."""
            with self.assertRaises(TypeError):
                self.calc.add(10, "five")

            with self.assertRaises(TypeError):
                self.calc.add("ten", 5)

class TestCalculatorSubtraction(unittest.TestCase):

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = Calculator()

    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers where the result is positive."""
        result = self.calc.subtract(15, 5)
        self.assertEqual(result, 10)

    def test_subtract_negative_numbers(self):
        """Test subtraction of two negative numbers."""
        result = self.calc.subtract(-10, -5)
        self.assertEqual(result, -5)

    def test_subtract_positive_and_negative(self):
        """Test subtraction of a positive and a negative number."""
        result = self.calc.subtract(10, -5)
        self.assertEqual(result, 15)

    def test_subtract_negative_and_positive(self):
        """Test subtraction of a negative and a positive number."""
        result = self.calc.subtract(-10, 5)
        self.assertEqual(result, -15)

    def test_subtract_resulting_in_negative(self):
        """Test subtraction where the result is negative."""
        result = self.calc.subtract(5, 10)
        self.assertEqual(result, -5)

    def test_subtract_zero(self):
        """Test subtraction when one of the operands is zero."""
        result = self.calc.subtract(10, 0)
        self.assertEqual(result, 10)

    def test_subtract_zero_from_negative(self):
        """Test subtraction of zero from a negative number."""
        result = self.calc.subtract(-5, 0)
        self.assertEqual(result, -5)

    def test_subtract_same_numbers(self):
        """Test subtraction of two identical numbers, resulting in zero."""
        result = self.calc.subtract(10, 10)
        self.assertEqual(result, 0)

class TestCalculatorMultiplication(unittest.TestCase):

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = Calculator()

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        result = self.calc.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_multiply_negative_numbers(self):
        """Test multiplication of two negative numbers."""
        result = self.calc.multiply(-4, -3)
        self.assertEqual(result, 12)

    def test_multiply_positive_and_negative(self):
        """Test multiplication of a positive and a negative number."""
        result = self.calc.multiply(7, -2)
        self.assertEqual(result, -14)

    def test_multiply_by_zero(self):
        """Test multiplication when one of the numbers is zero."""
        result = self.calc.multiply(5, 0)
        self.assertEqual(result, 0)

    def test_multiply_negative_and_zero(self):
        """Test multiplication of a negative number by zero."""
        result = self.calc.multiply(-8, 0)
        self.assertEqual(result, 0)

    def test_multiply_large_numbers(self):
        """Test multiplication of two large numbers."""
        result = self.calc.multiply(1000000, 1000000)
        self.assertEqual(result, 1000000000000)

    def test_multiply_by_one(self):
        """Test multiplication of a number by one."""
        result = self.calc.multiply(15, 1)
        self.assertEqual(result, 15)

class TestCalculatorDivision(unittest.TestCase):

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = Calculator()

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_negative_numbers(self):
        """Test division of two negative numbers."""
        result = self.calc.divide(-20, -4)
        self.assertEqual(result, 5)

    def test_divide_positive_by_negative(self):
        """Test division of a positive number by a negative number."""
        result = self.calc.divide(15, -3)
        self.assertEqual(result, -5)

    def test_divide_negative_by_positive(self):
        """Test division of a negative number by a positive number."""
        result = self.calc.divide(-15, 3)
        self.assertEqual(result, -5)

    def test_divide_by_zero(self):
        """Test division by zero, should return an error message."""
        result = self.calc.divide(10, 0)
        self.assertEqual(result, "Error: Division by zero is undefined.")

    def test_divide_zero_by_number(self):
        """Test division of zero by a number, result should be zero."""
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)

    def test_divide_fraction_result(self):
        """Test division that results in a fraction."""
        result = self.calc.divide(7, 2)
        self.assertEqual(result, 3.5)

class TestCalculatorDivision(unittest.TestCase):

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = Calculator()

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        result = self.calc.divide(20, 5)
        self.assertEqual(result, 4)

    def test_divide_negative_numbers(self):
        """Test division of two negative numbers."""
        result = self.calc.divide(-20, -5)
        self.assertEqual(result, 4)

    def test_divide_positive_by_negative(self):
        """Test division of a positive number by a negative number."""
        result = self.calc.divide(20, -5)
        self.assertEqual(result, -4)

    def test_divide_negative_by_positive(self):
        """Test division of a negative number by a positive number."""
        result = self.calc.divide(-20, 5)
        self.assertEqual(result, -4)

    def test_divide_by_zero(self):
        """Test division by zero, should return an error message."""
        result = self.calc.divide(10, 0)
        self.assertEqual(result, "Error: Division by zero is undefined.")

    def test_divide_zero_by_number(self):
        """Test division of zero by a number, result should be zero."""
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)

    def test_divide_fraction_result(self):
        """Test division resulting in a fraction."""
        result = self.calc.divide(7, 2)
        self.assertEqual(result, 3.5)



class Calculator:
    """Simple calculator class for demonstration."""

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is undefined."
        return a / b


class TestCalculatorDivision(unittest.TestCase):

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = Calculator()

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        result = self.calc.divide(20, 5)
        self.assertEqual(result, 4)

    def test_divide_negative_numbers(self):
        """Test division of two negative numbers."""
        result = self.calc.divide(-20, -5)
        self.assertEqual(result, 4)

    def test_divide_positive_by_negative(self):
        """Test division of a positive number by a negative number."""
        result = self.calc.divide(20, -5)
        self.assertEqual(result, -4)

    def test_divide_negative_by_positive(self):
        """Test division of a negative number by a positive number."""
        result = self.calc.divide(-20, 5)
        self.assertEqual(result, -4)

    def test_divide_by_zero(self):
        """Test division by zero, should return an error message."""
        result = self.calc.divide(10, 0)
        self.assertEqual(result, "Error: Division by zero is undefined.")

    def test_divide_zero_by_number(self):
        """Test division of zero by a number, result should be zero."""
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)

    def test_divide_fraction_result(self):
        """Test division resulting in a fraction."""
        result = self.calc.divide(7, 2)
        self.assertEqual(result, 3.5)


def run_test(test_method):
    suite = unittest.TestSuite()
    suite.addTest(TestCalculatorDivision(test_method))
    runner = unittest.TextTestRunner()
    runner.run(suite)


def show_menu():
    print("\nCalculator Division Test Menu:")
    print("1. Test division of two positive numbers")
    print("2. Test division of two negative numbers")
    print("3. Test division of positive by negative number")
    print("4. Test division of negative by positive number")
    print("5. Test division by zero")
    print("6. Test division of zero by a number")
    print("7. Test division resulting in a fraction")
    print("0. Exit")


def main6():
    while True:
        show_menu()
        choice = input("Enter your choice (0 to exit): ")

        if choice == '1':
            run_test("test_divide_positive_numbers")
        elif choice == '2':
            run_test("test_divide_negative_numbers")
        elif choice == '3':
            run_test("test_divide_positive_by_negative")
        elif choice == '4':
            run_test("test_divide_negative_by_positive")
        elif choice == '5':
            run_test("test_divide_by_zero")
        elif choice == '6':
            run_test("test_divide_zero_by_number")
        elif choice == '7':
            run_test("test_divide_fraction_result")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
