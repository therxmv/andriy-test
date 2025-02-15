from calculator import add, subtract, multiply, divide

def main():

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose and operation: (+, -, *, /): ")

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                return
        else:
            print("Unknown operation")
            return

        print(f"Result {result}")

    except ValueError:
        print("Uncorrect numbers")

if __name__ == "__main__":
    main()
