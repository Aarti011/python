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

# program to take user imput and get him a number acc to that
numb= int(input("Enter any number as per your choice : "))
class finder:
  def __init__(self, number):
    self.number=number
    print("This is your number : ", (number/2)+10,)
value=finder(numb)
  
