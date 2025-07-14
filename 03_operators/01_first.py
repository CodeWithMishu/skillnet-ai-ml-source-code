# and , or , not 
# membership operator:

# list =[1,3,4,5,]
# print(3 in list)

# list =[6,3,3,3,44,3]
# print(6 not in list)

# x =y = [1,2,3]
# # y= [1,2,3]
# print(x is y)


# some practice questions on and , or , in ,not in , is :
a = 33
if (a>=1 and a<=50):
    print("Good")
elif(a<0 or a==0):
    print("not good")

x = ["a","b","d"]
if("a" not in x):
    print(x)
print("c" not in x)

x = y = [1,2,3,4,4,5,5]
print(x is y)

fruits =["apple","pineapple","banana"]
# fruits.append("mango")
# print(fruits)
# fruits.insert(1,"orange")
# fruits.remove("banana")
# fruits.pop()
print(fruits)

port = [5,3,6,4,4]
# port.sort()
# port.reverse()

s ="Hello"
# print(len(s))
# print(s.upper())
# print(s.lower())

student = {
    "name":"Munish",
    "age":19


}
print(student["name"])

# student["grade"]="A" # to add key value in a data dictionary 
# print(student)

# print(student.get("age")) # to get value of any key in data dictionary

student_2 = {
"name":"Sahil",
"age":20
}
a =student.get("age")
b =student_2.get("age")
print(a+b)

# 10 students dictionary - name , age , roll number print seperately 
