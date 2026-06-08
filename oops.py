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
