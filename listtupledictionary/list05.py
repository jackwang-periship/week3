'''
Created on Jun 13, 2017

@author: jwang02
'''

L = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']

# The  operations that modify the list will modify it in place. 
# This means that if you have multiple variables that point to the same list, 
# all variables will be updated at the same time.

MyNewList = L
# modify both lists
L.append("Jack")
print L
print MyNewList

# To create a separate list, you can use slicing or the list function to quickly create a copy:
MyNewList = L[:]

# modify L only
L.append("Wang")
print L
print MyNewList

# the extend method adds items from another list (or any sequence) to the end, 
# and insert inserts an item at a given index, and move the remaining items to the right.

L.extend(fruits)
print L

MyNewList.insert(3, "AVTECH")
print MyNewList

#To insert items from another list or sequence at some other location, use slicing syntax:
MyNewList[1:3] = fruits
print MyNewList
