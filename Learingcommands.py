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


class Justtrying:
  def __init__(self, name, gender):
    self.name=name
    self.gender=gender
    
  def intro(self):
    return f"My name is {self.name} and I'm a {self.gender}"


p1=Justtrying("Alfiya", "female")
print(p1.name)
print(p1.gender)

print(p1.intro())

# Python Array
Arr= [11, 4, 6, 7, "Rithvik" , "Canada", "Malaika"] 
n=len(Arr)
for i in range(0,n):
  print(Arr[i] , end="\n")


# for Modules 
# first we make a python file
# then we import that python file in another python file and use its function or objects 

class Welcome:
  def __intit__(self, name1, name2, name3)
  self.name1=name1
  self.name2=name2
  self.name3=name3
    
  def greet1():
    return f"Hey {self.name1}, how was your day today?"
  def greet2():
    return f"Yo {self.name2}, It's nice meeting you again, how have u been these days?"
  def greet3():
    return f"Hi {self.name3}, I was wondering where have u gone, so here you are!"

a=Welcome("Rdhika", "Ramya", "Komal")
P1=a.greet1()
P2=a.greet2()
P3=a.greet3()
# save the file with .py extension let's say the name is "mod.py"

# now we have to import the file named "mod.py"
import mod.py as m
print(m.p1)
print(m.p2)
print(m.p3)











  
