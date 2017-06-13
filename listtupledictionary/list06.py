'''
Created on Jun 13, 2017

@author: jwang02
'''
'''
The del statement can be used to remove an individual item, 
or to remove all items identified by a slice. 
The pop method removes an individual item and returns it, 
while remove searches for an item, and removes the first matching item from the list.

The del statement and the pop method does pretty much the same thing, 
except that pop returns the removed item.
'''

L = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots', 'pears']

del L[3]
print L

del L[1:5]
print L

item = L.pop() # last item
print item
print

item = fruits.pop(0) # first item
print item
print fruits
print

item = fruits.pop(1)
print item
print fruits
print

fruits.remove(item)
print fruits

'''
The list has the following performance characteristics:

* The list object stores pointers to objects, not the actual objects themselves. 
  The size of a list in memory depends on the number of objects in the list, 
  not the size of the objects.
* The time needed to get or set an individual item is constant, 
  no matter what the size of the list is (also known as “O(1)” behaviour).
* The time needed to append an item to the list is “amortized constant”; 
  whenever the list needs to allocate more memory, 
  it allocates room for a few items more than it actually needs, to avoid having to reallocate on each call 
  (this assumes that the memory allocator is fast; 
  for huge lists, the allocation overhead may push the behaviour towards O(n*n)).
* The time needed to insert an item depends on the size of the list, or more exactly, 
  how many items that are to the right of the inserted item (O(n)). 
  In other words, inserting items at the end is fast, 
  but inserting items at the beginning can be relatively slow, if the list is large.
* The time needed to remove an item is about the same as the time needed to insert an item at the same location; 
  removing items at the end is fast, removing items at the beginning is slow.
* The time needed to reverse a list is proportional to the list size (O(n)).
* The time needed to sort a list varies; the worst case is O(n log n), 
  but typical cases are often a lot better than that. 

'''