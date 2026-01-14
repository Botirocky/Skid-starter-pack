def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")

    while True:
        try:                                              
            # Get first number
            num1 = input("Enter first number: ")
            if num1.lower() == 'quit':          
                break
            num1 = float(num1)

            # Get operation
            operation = input("Enter operation (+, -, *, /): ")
            if operation.lower() == 'quit':
                break
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please try again.")
                continue

            # Get second number
            num2 = input("Enter second number: ")
            if num2.lower() == 'quit':
                break
            num2 = float(num2)

            # Perform calculation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()
