# A class is a blueprint or a template for creating objects, providing intial values for state(member variables or attributes), and implementations of behavior(memeber functions or methods).
class Person:
  name = "Jacob"
  occupation = "Finance"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")

# The self parameter is a reference to the current instance of the class.

a=Person()
b=Person()
a.name="piyush"
a.occupation = "tester"
b.name = "mansi"
b.occupation = "Banker"

a.info()
b.info()
# print(a.name,a.occupation)