class Calculator:

    def __init__(self):
        pass

    def _execute_operation(self, choice, x, y):
        operations = {
            "1": lambda: x + y,
            "2": lambda: x - y,
            "3": lambda: x * y,
            "4": lambda: x / y if y != 0 else Calculator.error_statement(self),
            "5": lambda: x ** y
        }
        return operations[choice]()
        
    def greeting(self):
        return "Welcome to the Advanced Calculator!"

    def error_statement(self):
        return 'Error: Cannot divide by zero!'

    def exit_condition(self):
        return 'Thank you for using the calculator. Goodbye!'

    def invalid_condition(self):
        return 'Invalid input. Please try again.'

calculator = Calculator()

print(calculator.greeting())

while True:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Grading")
    print("6. Exit")

    choice = input("Enter the operation number (1/2/3/4/5/6): ")

    if choice == "6":
        print(calculator.exit_condition())
        break
    
    elif choice not in ("1", "2", "3", "4", "5"):
        print(calculator.invalid_condition())
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation_result = calculator._execute_operation(choice, num1, num2)
    print(f"Result: {operation_result}")

