# Python decorators are a powerful and versatile tool that aloow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method modifying its source code.

def greet(fx):
  def mfx():
    print("Good morning")
    fx()
    print("Goodnight")
  return mfx
  
@greet
def hello():
  print("Hello World")

def add(a,b):
  print(a+b)

hello()
