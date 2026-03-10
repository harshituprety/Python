# the filter function filters a sequence of elements based on a given predicate( a function that returns a boolean value) and returns a new sequnce containing only the elements that meet the practice

l = [2,4,6,8,10]

# def filter_function(a):
#   return a>4

newl = list(filter(lambda a:a>4,l))
print(newl) 
