'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
* Dictionary comprehension is an elegant and concise way to create 
  new dictionary from an iterable in Python.

* Dictionary comprehension consists of an expression pair (key: value) followed 
  by for statement inside curly braces {}.
  
* A dictionary comprehension can optionally contain more for or if statements.
  An optional if statement can filter out items to form the new dictionary.
  
'''
squares = {x: x*x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

# This is the same as:
squares = {}
for x in range(6):
    squares[x] = x*x

# contain for or if statements as filter
odd_squares = {x: x*x for x in range(11) if x%2 == 1}

# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(odd_squares)
