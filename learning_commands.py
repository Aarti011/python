# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
# ----------------------------------------------

class human:
  pass

p1 = Human()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)
# -----------------------------------------------

class son:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Lins", 28)

print(p1.name)
print(p1.age)
