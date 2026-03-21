# Getters in python are methods that are used to access the values of an object's properties.

class ShowClass:
  def __init__(self,value):
    self._value = value

  def show(self):
    print(f"This is the {self._value}")

  @property
  def ten_value(self):
    return 10* self._value

  @ten_value.setter
  def ten_value(self,new_value):
    self.value = new_value/10
  
obj = ShowClass(30)
obj.ten_value = 84
print(obj.ten_value)
obj.show()

