# List comprehesions are used for creating new lists from other iterables like lists, tuples,dictionaries,sets, and even in arrays and strings

lst = [i for i in range(30)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
 
cities = ["Lucknow", "Jaipur", "Mumbai", "Goa", "Shimla"]
cities_0 = [city for city in cities if "a" in city]
print(cities_0)