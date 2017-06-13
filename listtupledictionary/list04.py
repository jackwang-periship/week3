'''
Created on Jun 13, 2017

@author: jwang02
'''
from numpy.lib.function_base import average
'''
Looping Over Lists
'''

L = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']

# The for-in statement makes it easy to loop over the items in a list:

for item in L:
    print item

# If you need both the index and the item, use the enumerate function:

for index, item in enumerate(L):
    print index, item

# If you need only the index, use range and len:

for index in range(len(L)):
    print index

# The list object supports the iterator protocol. To explicitly create an iterator, 
# use the built-in iter function:

i = iter(L)
item = i.next() # fetch first value
print item
item = i.next() # fetch second value
print item

# Python provides various shortcuts for common list operations. 
# For example, if a list contains numbers, the built-in sum function gives you the sum:

total = sum(the_count)

print total

average = float(sum(the_count)) / len(the_count)

print average

# If a list contains strings, you can combine the string into a single long string 
# using the join string method:

s = ''.join(L)

print s
