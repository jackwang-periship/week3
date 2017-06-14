'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
* Use of Lambda Function
  We use lambda functions when we require a nameless function for a short period of time.
  In Python, we generally use it as an argument to a higher-order function 
  (a function that takes in other functions as arguments). 
  Lambda functions are used along with built-in functions like filter(), map() etc.
* Example use with filter()
  The filter() function in Python takes in a function and a list as arguments.
  The function is called with all the items in the list and a new list is returned 
  which contains items for which the function evaluats to True.
* The example use of filter() function to filter out only even numbers from a list.
'''
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)

