'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
* Syntax of Lambda Function

    lambda arguments: expression

  Lambda functions can have any number of arguments but only one expression. 
  The expression is evaluated and returned. 
  Lambda functions can be used wherever function objects are required.


'''

# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))