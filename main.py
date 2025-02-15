from calculator import add, subtract, multiply, divide, power

def main():
   
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -): ")

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "^":
            result = power(num1, num2)
        else:
            print("Unknown operation!")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Uncorrect numbers! ")

if name == "main":
    main()
