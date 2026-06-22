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








