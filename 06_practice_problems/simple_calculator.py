# Simple calculator without if-else statements
# Practice problem: Create calculator using dictionary and functions

# Calculator operations using dictionary
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

print("=== SIMPLE CALCULATOR ===")
print("Available operations: +, -, *, /")

# Get user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation using dictionary lookup
if operator in operations:
    result = operations[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")
else:
    print("Invalid operator")

# Alternative approach using eval (be careful with eval in real applications)
print("\n=== ALTERNATIVE APPROACH ===")
expression = input("Enter expression (e.g., 5 + 3): ")
try:
    result = eval(expression)
    print(f"Result: {result}")
except:
    print("Invalid expression")
