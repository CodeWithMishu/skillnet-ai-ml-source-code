#take user input and print this is the type and also print the input 
value = input("Enter any value: ")

# Try to detect the type
if value.lower() == "true":
    converted_value = True
    detected_type = type(converted_value)
elif value.lower() == "false":
    converted_value = False
    detected_type = type(converted_value)
else:
    try:
        converted_value = int(value)
        detected_type = type(converted_value)
    except ValueError:
        try:
            converted_value = float(value)
            detected_type = type(converted_value)
        except ValueError:
            try:
                converted_value = complex(value)
                detected_type = type(converted_value)
            except ValueError:
                converted_value = value
                detected_type = type(value)

print(f"You entered: {converted_value}")
print(f"Type of input: {detected_type}")