num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operand = input("Enter the operand (+,-,*,/):")
if operand =="+":
    print(num1+num2)
elif operand =="-":
    print(num1-num2)
elif operand =="*":
    print(num1*num2)
elif operand =="/":
    print(num1/num2)
else:
    print("invalid input")


