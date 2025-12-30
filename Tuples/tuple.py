# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas & enclosed within round brackets. Tuples are immutable.

tup = (1,3,57,36,49,182,32,"grey", True)

print(tup[:4])

print(type(tup))
print(len(tup))
print(tup[-3])
print(tup[2])
print(tup[1])

if True in tup:
  print("Yes tup is True")
else:
  print("No")

tup2 = tup[1:4]
print(tup2)