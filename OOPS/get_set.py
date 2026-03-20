# Getters in python are methods that are used to access the values of an object's properties.

class ShowClass:
  def __init__(self,value):
    self._value = value

  def show(self):
    print(f"This is the {self._value}")

  @property
  def value(self):
    return self._value
  
obj = ShowClass(30)
print(obj.value)

