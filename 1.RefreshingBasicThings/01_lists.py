"""
A list is used to store multiple items in a single variable
"""

my_list = ["apple", "melon", "tomatoe"]
print(my_list)
#Prints: ['apple', 'melon', 'tomatoe']

"""
A list prints all in the same order that you write in,
for exemple:
"""

my_list.append("onion")
print(my_list)
#Prints: ['apple', 'melon', 'tomatoe', 'onion']

"""
And we can insert some objects in a specific place:
"""

my_list.insert(2, "pineapple")
print(my_list)
#Prints: ['apple', 'melon', 'pineapple', 'tomatoe', 'onion']
