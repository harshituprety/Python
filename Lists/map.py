# The map function applies a function to each element in a sequence & returns a new sequence contaaining the transformed elements

# def cube(x):
#   return x*x*x

l = [2,4,6,8,10]

newl = list(map(lambda x:x*x*x,l))
print(newl);
