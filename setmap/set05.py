'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
* Union of A and B is a set of all elements from both sets.
Union is performed using | operator. 
Same can be accomplished using the method union().

* Intersection of A and B is a set of elements that are common in both sets.
Intersection is performed using & operator. 
Same can be accomplished using the method intersection().

* Difference of A and B (A - B) is a set of elements that are only in A but not in B. 
Similarly, B - A is a set of element in B but not in A.
Difference is performed using - operator. Same can be accomplished using the method difference().

* Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
Symmetric difference is performed using ^ operator. 
Same can be accomplished using the method symmetric_difference().

'''
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)



