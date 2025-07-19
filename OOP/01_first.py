# class myclass:
#     x = 5
# p1=myclass
# print(p1.x)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1 = person(name1="Tushar",age = 20)
# print(p1.name)
# print(p1.age)

def decorator1(func):
    print("Decorator is called")
    func()
    print("Decorator is finished")
    return decorator1
@decorator1
def my_function():
    print("Hello world")
my_function