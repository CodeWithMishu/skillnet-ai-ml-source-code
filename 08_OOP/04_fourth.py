# cls and self are nearby similar - self gives reference to object  and cls is used to give reference of class

# class Dog:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         Dog.count +=1
#     @classmethod
#     def total_dogs(cls):
#      print(f" Total Dogs :{cls.count}")
# d1 = Dog("sheru")
# d2 = Dog("Tiger")
# d3 = Dog("Tigerdfd")
# Dog.total_dogs()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls,student_str):
        name,age = student_str.split("--")
        return cls(name,int(age))
    
s1 = Student.from_string("Tushar--25")
print(s1.name)
print(s1.age)