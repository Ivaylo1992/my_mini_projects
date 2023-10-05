def exit_condition():
    return 'Thank you for using the calculator. Goodbye!'


def invalid_condition():
    return 'Invalid input. Please try again.'


def error_statement():
    return 'Error: Cannot divide by zero!'


def comparing(x, y):
    if x > y:
        return f'{x} > {y}'
    elif x < y:
        return f'{x} < {y}'
    else:
        return f'{x} = {y}'


def _execute_operation(choice, x, y):
    operations = {
        "1": lambda: x + y,
        "2": lambda: x - y,
        "3": lambda: x * y,
        "4": lambda: x / y if y != 0 else error_statement(),
        "5": lambda: x ** y,
        "6": lambda: x % y if y != 0 else error_statement(),
        "7": lambda: comparing(x, y),
    }
    return operations[choice]()


def calculator():
    print("Welcome to the Advanced Calculator!")

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Grading")
        print("6. Modulo")
        print("7. Comparing")
        print("8. Exit")

        choice = input("Enter the operation number (1/2/3/4/5/6/7/8): ")

        if choice == "8":
            print(exit_condition())
            break
        elif choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print(invalid_condition())
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        operation_result = _execute_operation(choice, num1, num2)
        print(f"Result: {operation_result}")


if __name__ == "__main__":
    calculator()
