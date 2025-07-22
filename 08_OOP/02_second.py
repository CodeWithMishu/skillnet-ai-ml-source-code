# _init_ is like constructor and it auto calls the object  
# _del_() it is like destructor 
# __str__ is a magic method 
# __repr_

# class Myclass():
#     x = 5
# p1 = Myclass()
# print(p1.x)

# class person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = person("Munish",25)
# p2 = person("Sahil",19)
# print(p1.name,p1.age)
        
# class person():
#     def __init__(self,name,age, city,course):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.course = course
# m1 = person("Munish",19,"Bilaspur","BCA")
# m2 = person("abhishek",23,"rerer","334")
# # m3 = name("Vishal")
# # m4 = name("sahil")
# print(m1.name)
# print(m1.age)
# print(m1.city)
# print(m1.course)

# class student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name},Age: {self.age}"
# p1 = student("Munish",19)
# # print(p1.name,p1.age)
# print(p1)


class student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def  __repr__(self):
        return f"Name: {self.name},Age: {self.age}"
p1 = student("Munish",19)
print(p1)