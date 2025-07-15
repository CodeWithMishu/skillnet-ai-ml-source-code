# Single student data dictionary with all 10 students using lists
student_data = {
    "name": [
        "Munish", "Sahil", "Abhisek", "Vishal", "Aditya", 
        "Mandeep", "Akshay", "Saurav", "Mohit", "Rohan"
    ],
    "age": [
        19, 18, 20, 19, 21, 
        18, 20, 19, 22, 18
    ],
    "roll_number": [
        101, 102, 103, 104, 105, 
        106, 107, 108, 109, 110
    ]
}

# Using get() function to access data
names = student_data.get("name")[0], student_data.get("age")[0], student_data.get("roll_number")[0]
print(names)
# print(ages)




# ages = student_data.get("age")
# roll_numbers = student_data.get("roll_number")


# print("All Student Data using get() function:")
# print(f"Names: {names}")
# print(f"Ages: {ages}")
# print(f"Roll Numbers: {roll_numbers}\n")

# # Access individual student data using get() and indexing
# print("Individual Student Information using get():")
# for i in range(10):
#     name = student_data.get("name")[i]
#     age = student_data.get("age")[i]
#     roll = student_data.get("roll_number")[i]
    
#     print(f"Student {i+1}:")
#     print(f"  Name: {name}")
#     print(f"  Age: {age}")
#     print(f"  Roll Number: {roll}\n")

# # Examples of accessing specific data using get()
# print("Examples of accessing specific data using get():")
# print(f"First student name: {student_data.get('name')[0]}")
# print(f"Last student age: {student_data.get('age')[9]}")
# print(f"Third student roll number: {student_data.get('roll_number')[2]}")

# # Using get() with default values for safety
# print(f"\nSafe access with default: {student_data.get('grade', 'Not Available')}")

