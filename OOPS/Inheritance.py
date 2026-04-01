# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have it's own properties and methods,this is called as inheritance.

class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id=id

  def showDetails(self):
    print(f"The details of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default language is javascript")


e1 = Employee('Manoj',933)
e1.showDetails()
e2 = Programmer('Kirti',988)
e2.showDetails()
e2.showLanguage()
