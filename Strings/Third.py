# String is a data type in python

# String is a sequence of characters enclosed in quotes

name = "Kathuria"

#! STRING SLICING

# A string in python can be sliced for getting a part of the strings

# String indexing start from 0 and start from -1 if counted in reverse 

#* sl = name[ind_start:ind-end]
#* sl[0:3] returns "kat" --> characters from 0 to 3
#* sl[1:3] returns "at" --> characters from 1 to 3

# last index is not included in slice of string

string_len = len(name)

print(string_len)

namecut = name[0:3]

print(namecut)

print(name[-4:-1])
print(name[4:7])

print(name[:4]) #! is same as print(name[0:4])
print(name[1:]) #! is asame as print(name[1:8])
print(name[1:8])