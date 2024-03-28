def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

choice = ['+', '-', '*', '/']
calculate = True

while calculate:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation in choice:
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        print(f"The result is: {result}")
    else:
        print("Invalid operation")

    user_choice = input("Do you want to continue? (yes/stop): ").lower()
    if user_choice == "stop":
        calculate = False
    elif user_choice != "yes":
        print("Invalid choice. Exiting...")
        calculate = False