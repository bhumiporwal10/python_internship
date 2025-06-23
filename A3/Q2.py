def basic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero")

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
basic_operations(num1, num2)
