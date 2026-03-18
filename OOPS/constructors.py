# A constructor is a special method in a class used to create and initialize an object of a class. A constructor is a unique function that gets called automatically when an object is created of a class. 

class Person:

  def __init__(self,name,occupation):
    print("Hey! How are you")
    self.name = name
    self.occupation = occupation

  def info(self):
    print(f"{self.name} is a {self.occupation}")

a=Person("Girish","Accountant")
b=Person("Manish","Salesman")

a.info()
b.info()