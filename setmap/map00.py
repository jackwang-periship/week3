'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
* The syntax of map() is:

map(function, iterable, ...)

* map() Parameter

    function - map() passes each item of the iterable to this function.
    iterable iterable which is to be mapped

You can pass more than one iterable to the map() function.

* Return Value from map()

The map() function applies a given to function to each item of an iterable 
and returns a list of the results.

The returned value from map() (map object) then can be passed to functions like list() 
(to create a list), set() (to create a set) and so on.
'''
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
