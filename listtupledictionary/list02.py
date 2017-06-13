'''
Created on Jun 13, 2017

@author: jwang02
'''

L = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']

# Lists implement the standard sequence interface; len(L) returns the number of items in the list, 
# L[i] returns the item at index i (the first item has index 0), 
# and L[i:j] returns a new list, containing the objects between i and j.

n = len(L)
print n

item = L[2]
print item

seq = L[2:6]
print seq

# If you pass in a negative index, Python adds the length of the list to the index. 
# L[-1] can be used to access the last item in a list.

# For normal indexing, if the resulting index is outside the list, 
# Python raises an IndexError exception. Slices are treated as boundaries instead, 
# and the result will simply contain all items between the boundaries.
# Lists also support slice steps:
 
seq = L[1:7:2]
print seq

# get every other item, starting with the first
seq = L[::2]
print seq

# get every other item, starting with the second
seq = L[1::2]
print seq
 

