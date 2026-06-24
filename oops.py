class Animal:
    species = "Dog" 

    def __init__(self, name, age):
        self.name = name  
        self.age = age
        
# Creating an object of the Dog class
dog1 = Animal("Buddy", 3)
print(dog1.name) 
print(dog1.species)

# Inheritance in OOPs
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()


# Python oops  new program

class Person:
    def __init__(self, name, roll, standard):
        self.name=name
        self.roll=roll
        self.standard=standard

stud1= Person("Anshika", 56, 7)
print(stud1.name , stud1.roll, stud1.standard)

stud2=Person("Manoj", 64, 7)
print(stud2.name)
print(stud2.roll)
print(stud2.standard)

stud3=Person("Kanishq", 23, 7)
print(stud3.name)
print(stud3.roll)
print(stud3.standard)


# python code for inheritance
class Inherit
    def parent(self):
        print("He is the father")
class Passer(Inherit):
    def child(self):
        print("Now this is the child)
s1= Inherit()
s1.parent()

s3 = Passer()
s3.parent()



# python code for abstraction
from abc import ABC, abstractmethod
class Booker(ABC):
    @abstractmethod
    def greet(self):
        pass
class Book(Booker):
    def greet(self):
        print("That's a hypocrate")
s1=Book()
s1.greet()
    


from abc import ABC, abstractmethod 
class People:
    @abstractmethod
    def Boy(self):
        pass
class People2: 
    def Boy(self):
        print("This is all about Boy")
p2=People2()
p2.Boy()
























