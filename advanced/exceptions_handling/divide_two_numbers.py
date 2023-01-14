def divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        result = None
    return result


if __name__ == '__main__':

    print(divide(4, 2))  # Output: 2.0
    print(divide(4, 0))  # Output: "Cannot divide by zero."
