# If you want to add, remove or change tuple to a list. Then perform operations on that list & convert it back to tuple 

brands = ("Nike", "Walmart", "Toyota", "Xiaomi", "Aramco")

temp = list(brands)
temp.append("Intel")
temp.pop(3)
temp[2] = "Honda"
brands = tuple(temp)
print(brands)

brands2 = ("Samsung", "Apple", "Shell")
new_brands = brands + brands2
print(new_brands)

tuple1 = (0,3,4,8,2,1,8,3,5,8)
res = tuple1.count(8)
res=tuple1.index(8,4,9)
print("count of 8 in tuple1 is:",res)
res = len(tuple1)
print(res)