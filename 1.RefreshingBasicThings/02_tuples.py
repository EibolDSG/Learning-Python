"""
A tuple is really near to a list but in this case we doesn't have the same
liberty to modify it
"""

my_tuple = ("apple", "melon", "tomatoe")
print(my_tuple)
#Prints: ('apple', 'melon', 'tomatoe')

"""
Lets try to append or insert anything in our tuple:
"""

#my_tuple.append("onion")
#AttributeError: 'tuple' object has no attribute 'append'

#my_tuple.insert(3, "onion")
#AttributeError: 'tuple' object has no attribute 'insert'

"""
The only thins we can do on our tuples are:
"""

my_tuple_count = my_tuple.count("melon")
print(my_tuple_count)
#Prints: 1

my_tuple_index = my_tuple.index("tomatoe")
print(my_tuple_index)
#Prints: 2 (Prints which index has the object I asked for)
