"""
A dictionary is used to store data values in key-value pairs
"""

my_dict = {"Fruit" : "Strawberry", "Vegetable" : "Tomatoe", "Animal" : "Ham" }
print(type(my_dict))
#Prints: <class 'dict'>
print(my_dict)
#Prints: {'Fruit': 'Strawberry', 'Vegetable': 'Tomatoe', 'Animal': 'Ham'}

"""
If we know the keys of our dict, we can search which is the value:
"""

print(my_dict["Vegetable"])
#Prints: Tomatoe

"""
And we can change it:
"""

my_dict["Vegetable"] = "Onion"
print(my_dict["Vegetable"])
#Prints: Onion

"""
We can extract the keys of our dict
"""

print(my_dict.keys())
#Prints: dict_keys(['Fruit', 'Vegetable', 'Animal'])

"""
And of course, the values
"""

print(my_dict.values())
#Prints: dict_values(['Strawberry', 'Onion', 'Ham'])
