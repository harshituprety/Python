
#! union() & update()
# The union() method  returns a new set whereas update() method adds items intoexisting set from another set

a = {3,2,9,8}
b = {7,4,6,1}
print(a.union(b))
a.update(b)
print(a,b)

c = a.intersection(b)
print(c)

brands = {"Nike", "Adidas", "Puma", "Reebok"}
brands2 = {"Adidas", "Asics", "Umbro", "Nike"}
brand = brands.intersection(brands2)
print(brand)
brands.intersection_update(brands2)
print(brands)

#! symetric_difference & symmetric_difference_update():
# The symmetric_difference_update() method updates into the existing set from another set whereas symmetric difference() method returns a new set

brands = {"Nike", "Adidas", "Puma", "Reebok"}
brands2 = {"Adidas", "Asics", "Umbro", "Nike"}
brand = brands.symmetric_difference(brands2)
print(brand)
brands.symmetric_difference_update(brands2)
print(brands)

#! isdisjoint():
# The isdisjoint() method checks if ites of given set are present in another set. This method returns Flase if items are present, else it returns True

brands = {"Nike", "Adidas", "Puma", "Reebok"}
brands2 = {"New Balance", "Asics", "Umbro", "Fila"}
brand = brands.isdisjoint(brands2)
print(brand)

#! issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False

brands = {"Nike", "Adidas", "Puma", "Reebok"}
brands2 = {"Adidas", "Asics", "Umbro", "Nike"}
print(brands.issuperset(brands2))
brand = {"Puma", "Reebok"}
print(brand.issubset(brands))

#! issubset():
#  The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False

brands = {"Nike", "Adidas", "Puma", "Reebok"}
brands2 = {"Adidas", "Nike"}
print(brands2.issubset(brands))

#! add():
# If want to add a single item

brands = {"Nike", "Adidas", "Puma", "Reebok"}
brands.add("Shimano")
print(brands)

#! remove() and discard():
brands = {"Nike", "Adidas", "Puma", "Reebok"}
brands.remove("Nike")
print(brands)
brands.discard("Nike")
print(brands)

#! pop():
brands = {"Nike", "Adidas", "Puma", "Reebok"}
item = brands.pop()
print(brands)
print(item)

#! del:
brands = {"Nike", "Adidas", "Puma", "Reebok"}
# del brands
print(brands)

#! clear():
brands = {"Nike", "Adidas", "Puma", "Reebok"}
brands.clear()
print(brands)






