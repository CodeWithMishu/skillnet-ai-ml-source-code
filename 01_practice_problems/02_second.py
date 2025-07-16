# Marriage calculator using gender, age, if-else, and loop

while True:
    gender = input("Enter your gender (male/female): ").lower()
    age = int(input("Enter your age: "))

    if gender == "male":
        if age >= 21:
            print("You are eligible for marriage!")
        else:
            print("Not eligible for marriage. ")
    elif gender == "female":
        if age >= 18:
            print("You are eligible for marriage!")
        else:
            print(f"Not eligible for marriage.")
    else:
        print("Invalid input check again . ")
