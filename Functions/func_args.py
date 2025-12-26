#  There are four types of arguments that we can provide in a function

#! Default Arguments
def average(a,b):
  print("The average is ", (a+b)/2)
  
average(3,9)

#! Keyword Arguments:-
average(b=5,a=8)

# ! Variable length Arguments:-

  #* Arbitrary Arguments:-
def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum+i
  print("Average is: ", sum / len(numbers)) 
  

  #* Keyword Arbitrary Argumnets:-

def name(**name):
  print(type(name)) 
  print("Hello", name["fname"], name["mname"], name["lname"])

name(mname="Faggan", lname="singh", fname="Kulsate" )

#! Required Arguments:-
def average(a,b,c=6):
  print("The average is ", (a+b+c)/2)

average(4,8)

#! Return Statement:-
def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum+i
  # print("Average is: ", sum / len(numbers)) 
  # return 8
  return sum / len(numbers)
  
c = average(4,2,6,8)
print(c)