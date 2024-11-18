#using classses

class MyClass:

    def __init__(self , name, age):
        self.name = name
        self.age = age


name = input("Name: ")
age = int(input("Age: "))
p1 = MyClass()
print(p1.x)