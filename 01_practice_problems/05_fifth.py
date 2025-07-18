# Q1 Create a function greet(name) that prints “Hello, [name]!”
def greet(name):
    print(f" Hello , {name}")
greet("Munish")


# Q2. Create a function add(a, b) that returns the sum of two numbers. Call the function with inputs.
def add(a,b):
    return a+b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print( f" The sum of {num1} and {num2} is : {add(num1,num2)}")

# Q3. Create a function display(*args) that accepts multiple arguments and prints them.
def display(*args):
    print(f" My name is {args[0]}, i am {args[1]} student and skilled in {args[2]} .")
display("Munish","BCA","Web Development")

# Q4. Create a function student_info(**kwargs) that accepts name, age, roll number as keyword arguments and prints them.
def student_info(**kwargs):
    print(f"My name is {kwargs["name"]}, and i am {kwargs["age"]} old and my roll number is {kwargs["roll_number"]}")

student_info(name="Munish Kumar Sharma",age="19",roll_number= "H240114")
