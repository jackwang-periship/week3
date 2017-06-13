'''
Created on Jun 13, 2017

@author: jwang02
'''
'''
We can access a range of items in a tuple by using the slicing operator - colon ":".

Slicing can be best visualized by considering the index to be between the elements as shown below. 
So if we want to access a range, 
we need the index that will slice the portion from the tuple.
'''
my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])