'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
delete or remove elements from a dictionary?

We can remove a particular item in a dictionary by using the method pop(). 
This method removes as item with the provided key and returns the value.

The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. 
All the items can be removed at once using the clear() method.

We can also use the del keyword to remove individual items or the entire dictionary itself.

* Python Dictionary Methods and description
clear()     Remove all items form the dictionary.
copy()     Return a shallow copy of the dictionary.
fromkeys(seq[, v])     Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])     Return the value of key. If key doesnot exit, return d (defaults to None).
items()     Return a new view of the dictionary's items (key, value).
keys()     Return a new view of the dictionary's keys.
pop(key[,d])     Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
popitem()     Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d])     If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
update([other])     Update the dictionary with the key/value pairs from other, overwriting existing keys.
values()     Return a new view of the dictionary's values

'''
# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
# Output: 16
print(squares.pop(4))  

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
del squares[5]  

# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
# print(squares)

marks = {}.fromkeys(['Math','English','Science'], 1)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
print list(sorted(marks.keys()))
