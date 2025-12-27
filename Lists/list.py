# List are ordered collection of data items.
# They store multiple items in  asingle variable
# List items are separated by commas & enclosed within square brackets []
# Lists are changeable meaning we can alter them after creation

l = [3,2,1,"gaurav", False, "joshi", 34, True]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

#! Accessing list items
#* Positve Indexing
print(l[5-3])
print(l[2])
#* Negative Indexing
print(l[-3])
print(l[len(l)-3])

if "gaurav" in l:
  print("Yes")
else:
  print("No")

if "rav" in "gaurav":
  print("Yes")

#? Range of Index:
# Can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range

#* listname[start : end : jumpIndex]

print(l[1:8])

#! print(l[0:len(l)])

print(l[1:8:2])
