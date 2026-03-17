# The reduce function is a higher corder function that applies a function to a sequence and returns a single value.

from functools import reduce

numbers = [3,5,7,9]

# def sum(x,y):
#   return x+y

newl = reduce(lambda x,y:x+y,numbers)

print(newl)