

# By default object instance cn be access as it's public access modifier
# private object instace cannot be access outside the class
# protected can be access within the class or sub-class  

class Employee:
  def __init__(self):
    self.name = 'Joseph'

a = Employee()
print(a.name)

# (__) double underscore is used to indicate private access which have weak integration cannot be access directly but can be access indirectly

class Employee:
  def __init__(self):
    self.__name='Manish'

a = Employee()
# print(a.__name)
print(a._Employee__name)

# Name mangling is a technique used to protect class-private and sub-class from beign accidently overwritten by subclasses.

class Student():
  def __init__(self,age,name):
    self.age = age
  
  def __funName(self):
    self.x=10
    print(self.y)

class Subject(Student):
  pass

a = Student(32,'Bhushan')
a1 = Subject

print(a.__age)
print(a.__funName())

print(a1.__age)
print(a1.__funName())

# Single underscore(_) is used as prefix in protected access 

class Student:
  def __init__(self):
    self._name = 'Namit'

  def _funcName(self):
    return 'Goodnight'

class Subject(Student):
  pass

a= Student()
a1 = Subject()


print(a._name)
print(a._funcName())

print(a1._name)
print(a1._funcName())
