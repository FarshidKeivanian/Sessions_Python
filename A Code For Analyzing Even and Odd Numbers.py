def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def sum_is_even(num1, num2):
    """Check if the sum of two numbers is even."""
    return is_even(num1 + num2)

def main():
    # Example numbers
    num1 = 4
    num2 = 6
    num3 = 5
    num4 = 7

    print(f"The sum of {num1} and {num2} is even: {sum_is_even(num1, num2)}")
    print(f"The sum of {num3} and {num4} is even: {sum_is_even(num3, num4)}")

if __name__ == "__main__":
    main()
