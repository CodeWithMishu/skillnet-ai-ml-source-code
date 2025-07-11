x=5
print(type(x)) #int
x="Munish"
print(type(x)) #str
x="22.2"
print(type(x)) #str
x=22.3
print(type(x)) #float
x=2j
print(type(x)) #complex
x=["Priyanshu"]
print(type(x))
x=("priyanshu","Munish") #typple can not be single multiple items 
print(type(x))
x=range(5)
print(type(x)) #range
x={"apple"}
print(type(x)) #set
x={"Name":"apple","Age":"19"}
y={"fruit":"apple",}
print(type(x)) #dictionary
print(x)
print(y)

x=frozenset({"apple","banana"}) #immutable version of data dictionary to give key name 
print(type(x))
x=True
print(type(x)) #boolean 

x=b"shivani"
print(type(x)) #bytes

x=memoryview(bytes(5))
print(type(x)) #memoryview
# print(x)

