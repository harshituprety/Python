def calcGmean(a,b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreat(a,b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")
    
def isLesser(a,b):
  pass

a = 9
b = 5
isGreat(a,b)
calcGmean(a,b)

c = 3
d = 3
isGreat(c,d)
calcGmean(c,d)