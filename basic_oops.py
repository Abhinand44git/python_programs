'''
class Student:
    def display(self):
        print("I am a student")
student = Student() #object creation
student.display()

class Employee:
    def __init__(self):
        print("Default Constructor is called")
employee = Employee()

class Car:
    color="Red" #class variable
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
car=Car("Pagani","Zonda")
print(car.brand,car.model,car.color)

car1=Car("Kia","Seltos")
print(car1.brand,car1.model,car1.color)
'''
class Library:
    def __init__(self,name,location="Trivandrum",total_books=0):
        self.name = name
        self.location = location
        self.total_books = total_books
library=Library("cherry Tree")
print(library.name,library.location,library.total_books)
library1=Library("Solo Leveling","Seoul")
print(library1.name,library1.location,library1.total_books)

library2=Library("Tensura","Kyoto",400000)
print(library2.name,library2.location,library2.total_books)