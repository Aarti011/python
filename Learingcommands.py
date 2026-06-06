# class properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


# acess properties
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)


# modify properties 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)

# program to take user input and get him a number acc to that
numb= int(input("Enter any number as per your choice : "))
class finder:
  def __init__(self, number):
    self.number=number
    print("This is your number : ", (number/2)+10,)

# general code for function
def greeting(name1, name2, name3):
    print("Hey hello mate how u doing :", name1, "\n")
    print("Hey hello mate what'sup :" , name2, "\n")
    print("Hey hello mate how have u been : ", name3, "\n")
greeting("Ankur", "Bhavya", "Kuromi kurdasiya")
value=finder(numb)

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())














  
