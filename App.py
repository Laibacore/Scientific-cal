import math

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

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def log(x, base=10):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Example usage
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")

choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num1} ^ {num2} = {power(num1, num2)}")

elif choice == '6':
    num = float(input("Enter number: "))
    print(f"√{num} = {square_root(num)}")

elif choice == '7':
    num = float(input("Enter number: "))
    base = float(input("Enter logarithm base (default is 10): ") or 10)
    print(f"log{base}({num}) = {log(num, base)}")

elif choice == '8':
    num = float(input("Enter number (in degrees): "))
    print(f"sin({num}) = {sin(num)}")

elif choice == '9':
    num = float(input("Enter number (in degrees): "))
    print(f"cos({num}) = {cos(num)}")

elif choice == '10':
    num = float(input("Enter number (in degrees): "))
    print(f"tan({num}) = {tan(num)}")

else:
    print("Invalid input")
