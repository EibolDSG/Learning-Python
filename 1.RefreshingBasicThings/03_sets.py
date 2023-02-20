"""
A set is another way to store items in a single variable but in this case,
they will change the index in a random way
"""

my_set = {"apple", "melon", "tomatoe"}
print(my_set)
#First print: {'melon', 'tomatoe', 'apple'}
#Second print: {'tomatoe', 'apple', 'melon'}

"""
In this case we CAN add values
"""

my_set.add("onion")
print(my_set)
#First print: {'melon', 'tomatoe', 'apple', 'onion'}
#Second print: {'tomatoe', 'onion', 'apple', 'melon'}

"""
An advantage of sets is that they don't admit repeated values
"""

my_set.add("onion")
print(my_set)
#First print: {'melon', 'tomatoe', 'apple', 'onion'}
#Second print: {'tomatoe', 'onion', 'apple', 'melon'}
