# Take user input and print the type and input
value = input("Enter any value: ")

# Check what type of input it is
if value.lower() == "true" or value.lower() == "false":
    print(f"You entered: {value}")
    print("Type of input: <class 'bool'>")
elif value.isdigit():
    print(f"You entered: {value}")
    print("Type of input: <class 'int'>")
elif value.count('.') == 1 and value.replace('.', '').isdigit():
    print(f"You entered: {value}")
    print("Type of input: <class 'float'>")
elif 'j' in value.lower():
    print(f"You entered: {value}")
    print("Type of input: <class 'complex'>")
else:
    print(f"You entered: {value}")
    print("Type of input: <class 'str'>")