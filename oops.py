class Animal:
    species = "Dog"  

    def __init__(self, name, age):
        self.name = name  
        self.age = age  

# Creating an object of the Dog class
dog1 = Animal("Buddy", 3)
print(dog1.name) 
print(dog1.species)
