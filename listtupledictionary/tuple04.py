'''
Created on Jun 13, 2017

@author: jwang02
'''
my_tuple = (4, 2, 3, [6, 5])
'''
Unlike lists, tuples are immutable.

This means that elements of a tuple cannot be changed once it has been assigned. But, 
if the element is itself a mutable datatype like list, its nested items can be changed.

We can also assign a tuple to different values (reassignment).
'''
# we cannot change an element
# If you uncomment line 8
# you will get an error:
# TypeError: 'tuple' object does not support item assignment

#my_tuple[1] = 9

# but item of mutable element can be changed
# Output: (4, 2, 3, [9, 5])
my_tuple[3][0] = 9
print(my_tuple)

# tuples can be reassigned
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple)
