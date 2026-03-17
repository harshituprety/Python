name = 'Avinash'
for i in name:
  print(i)
  if(i=='v'):
    print('This is something Awesome!')

colors = ["red","voilet","yellow","green"]

for color in colors:
  print(color)
  for i in color:
    print(i)

for k in range(5):
  print(k+1)

for k in range(1,2001):
  print(k)

for k in range (1,15,2):

  print(k)

#! Python allows the else keyyword yo be ued with the for and while loops too. The else block appears after the body of the loop.


for i in range(6):
  print(i)
else:
  print("Sorry no i")

for i in range(9):
  print(i)
  if i==4:
    break
  
else:
  print("Sorry no i")

i= 0
while i<7:
  print(i)
  i=i+1
  if i==4:
    break
  
else:
  print("Sorry no i")
