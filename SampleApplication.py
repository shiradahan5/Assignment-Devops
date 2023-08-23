import argparse
import unittest


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        print("test_addition")
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)


def test_multiplication(self):
    print("test_multiplication")
    self.assertEqual(multiply_numbers(2, 3), 6)
    self.assertEqual(multiply_numbers(0, 5), 0)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculator')
    parser.add_argument('operation', choices=['add', 'multiply'],
                        help='Choose the operation (add/multiply)')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')

    args = parser.parse_args()

    if args.operation == 'add':
        result = add_numbers(args.a, args.b)
        print(f"The sum of {args.a} and {args.b} is: {result}")
    else:
        result = multiply_numbers(args.a, args.b)
        print(f"The product of {args.a} and {args.b} is: {result}")

    # Run the tests
    # unittest.main()

# import argparse
# import unittest
#
# def add_numbers(a, b):
#     result = a + b
#     print(f"The sum of {a} and {b} is: {result}")
#     return result
#
# def multiply_numbers(a, b):
#     result = a * b
#     print(f"The product of {a} and {b} is: {result}")
#     return result
#
# class TestCalculator(unittest.TestCase):
#     def test_addition(self):
#         self.assertEqual(add_numbers(2, 3), 5)
#         self.assertEqual(add_numbers(-1, 1), 0)
#
#     def test_multiplication(self):
#         self.assertEqual(multiply_numbers(2, 3), 6)
#         self.assertEqual(multiply_numbers(0, 5), 0)
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Calculator')
#     parser.add_argument('operation', choices=['add', 'multiply'], help='Choose the operation (add/multiply)')
#     parser.add_argument('a', type=float, help='First number')
#     parser.add_argument('b', type=float, help='Second number')
#
#     args = parser.parse_args()
#
#     if args.operation == 'add':
#         result = add_numbers(args.a, args.b)
#     else:
#         result = multiply_numbers(args.a, args.b)
#
#     unittest.main()  # Run the tests when the script is executed
#
# # if __name__ == '__main__':
# #     parser = argparse.ArgumentParser(description='Calculator')
# #     parser.add_argument('operation', choices=['add', 'multiply'], help='Choose the operation (add/multiply)')
# #     parser.add_argument('a', type=float, help='First number')
# #     parser.add_argument('b', type=float, help='Second number')
# #
# #     args = parser.parse_args()
# #
# #     if args.operation == 'add':
# #         result = add_numbers(args.a, args.b)
# #     else:
# #         result = multiply_numbers(args.a, args.b)
#
#
#
#
#
#
# # # Example usage
# # num1 = 5
# # num2 = 7
# # result = add_numbers(num1, num2)
# #
# #
# #
# #
# # if __name__ == '__main__':
