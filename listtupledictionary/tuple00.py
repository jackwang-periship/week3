'''
Created on Jun 12, 2017

@author: jwang02
'''
'''
* We generally use tuple for heterogeneous (different) datatypes and list 
  for homogeneous (similar) datatypes.
* Since tuple are immutable, iterating through tuple is faster than with list. 
  So there is a slight performance boost.
* Tuples that contain immutable elements can be used as key for a dictionary. With list, 
  this is not possible.
* If you have data that doesn't change, implementing it as tuple will guarantee 
  that it remains write-protected.
* Having one element within parentheses is not enough. 
  We will need a trailing comma to indicate that it is in fact a tuple.
'''
# empty tuple
# Output: ()
my_tuple = ()
print(my_tuple)

# tuple having integers
# Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = my_tuple
print(a)
print(b)
print(c)

# only parentheses is not enough
# Output: <class 'str'>
my_tuple = ("hello")
print(type(my_tuple))

# need a comma at the end
# Output: <class 'tuple'>
my_tuple = ("hello",)  
print(type(my_tuple))

