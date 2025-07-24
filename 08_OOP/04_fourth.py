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

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def from_string(cls,student_str):
#         name,age = student_str.split("--")
#         return cls(name,int(age))
    
# s1 = Student.from_string("Tushar--25")
# print(s1.name)
# print(s1.age)

# class Animal:
#     def __init__(self,name):
#         # self.name = name
#         print(f"Animal created : {name}")
# class Dog(Animal):
#     def __init__(self, name , bread):
#         super().__init__(name)
#         # self.bread = bread
#         print(f"Dog created : {name}, son of {bread}")
# d = Dog("sheru","Dogesh")
# d.name
# d.bread

# class Math:
#     @staticmethod  # static method is used to call the class without using object we will not create a object here direct call using class and function 
#     def add(x,y):
#         return x+y
#     def sub(x,y):
#         return x-y
# print(Math.add(int(input("Enter first no.")),int(input("Enter second no."))))
# print(Math.sub(5,3))

#ininstance() and issubclass()

# class Animal:
#   pass
# class Dog(Animal):
#   pass
# d = Dog()
# print(isinstance(d,Dog)) #True
# print(isinstance(d,Animal)) # True
# print(issubclass(Animal,Dog)) # False
# print(issubclass(Dog,Animal)) # True

# class vehical:
#     def __init__(self,name):
#         self.name = name
#     def start(self):
#         print(f"{self.name} is starting ....")
# class Car(vehical):
#     def __init__(self, name,model):
#         super().__init__(name)
#         self.model = model
#     def start(self):
#         print(f"{self.name} , {self.model} is startingg.......")
# veh = vehical("Rolls_Royce")
# veh.start()

# c = Car("Mercdes","Benz S-class")
# c.start()

# class person:
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         if age>0:
#             self.__age = age
#         else:
#             print("invalid age")

# p = person("Munish",19)
# print(p.name)
# print(p.age)

# p.set_age(25)
# print(p.name)
# print(p.get_age())

# p.__age = 5
# print(p.get_age)