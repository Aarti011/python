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
    

#  Another similar code for abstraction
from abc import ABC, abstractmethod 
class People(ABC):
    @abstractmethod
    def Boy(self):
        pass
class People2(People): 
    def Boy(self):
        print("This is all about Boy")
p2=People2()
p2.Boy()



#  code for encapsulation in python

class Student:
    def __init__(self):
        self.__marks=85 #private variable
    def Marking(self):
        print(f"Marks= ", self.__marks)

ss= Student()
ss.Marking()



# Encapsulation Python another code
class PP:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def Peoplep(self):
        print(f"The value of x and y is as given {self.x}, {self.y}")
p1=PP(20,40)
p1.Peoplep()

# Python code for opening a file and writing somthing and reading

# writing in file
file1 =open(Python.txt,"w")
text= input("Enter any text: ")
file1.write(text)
file1.write("\nHelloo! there are more to explore...")
file1.close()

# reading from file
file2 = open(Python.txt, "r")
data=file2.read()
print(data)
file2.close()

# other way to read from file
with open("Python.txt", "w") as fileA:
    print(fileA.read())
fileA.close()



# counting total number of characters in file
with open("filename.txt", "r") as f1:
    readingfile=f1.read()
    counting= len(readingfile)
    print(f"Total number of words in the python file {counting}")



# reading file line by line
with open("Python.txt", "r") as f_A :
    for line in f_A:
        print(line)
f_A.close()



# counting total number of words in the file
with open("filename.txt","r") as f:
    content=f.read()
    words=content.split()
    count= len(words)
    print(count)
f.close()

# copy contents of one file to another
with open("filename.txt", "w") as f:
    f1= f.write("There are multiples ways to do the work but people chose to do it the way they find. \nThe people who chose to stand out are the one who put extra efforts and those are the people who are genuinly unique and loves to work hard to get the word done in a good way in order to achiever good outcome. \nWhile there are people who always look to procastinate and find easiest way so they get the things done in same way- not so satisfied.")
f.close()

with open("filename.text", "r")as ff:
    data=ff.read()
with open("file2.txt", "w") as fff:
    fff1=fff.write(data)
ff.close()
fff.close()
print("file content copied!")


# to read only the first line of the file content 
with open("filename.text", "r")as ff:
    data=ff.readline()
    print(data)
ff.close()



# Input multiple datas in the file 
with open("filename.text", "w")as ff:
    for i in range(3):
        inp=input("Enter the data")
        content=ff.write(inp)
for line in ff:
    print(line)
ff.close()
















