# Create 4 functions for +*/- and make a calculator use function calling for calculation symbols
def sum(num1,num2):
    return num1+num2
def diff(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
operand = input("Enter your operand (/,*,+,-) :")
number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number :"))
if operand=="+":
    print(sum(number1,number2))
elif operand=="-":
    print(diff(number1,number2))
elif operand=="*":
   print( multiply(number1,number2))
elif operand=="/":
    print(divide(number1,number2))
else:
    print("invalid input")