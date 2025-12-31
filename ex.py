# Create a oython program capable of greeting you with Good Morning, Good Afternoon, Good Evening. Your program should use time module to get the current hour.

import time

t = time.strftime("%H:%M:%S")
h = int(time.strftime("%H"))
h= int(input("Enter time:"))
print(h)


if(h>0 and h<12):
  print("Good Morning")
elif(h>12 and h<18):
  print("Good Afternoon")
elif(h>18 and h):
  print("Good Evening")