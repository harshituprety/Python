# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-vlaue pairs that are separated by commas and enclosed within curly brackets{}.

dict = {
  'name': 'Monty',
  'age': 18,
  'email': 'mty@gmail.com'
}
print(dict)
print(dict.keys())
print(dict.values())

# print(dict['email2'])
print(dict.get('email2')) #! prints none if key doesn't exist

# for key in dict.keys():
#   print(f"The value corresponding to the {key} is {dict[key]}")

print (dict.items())

for key,value in dict.items():
  print (f"the value correspondinig to the key {key} is {value}")