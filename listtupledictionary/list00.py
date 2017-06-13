'''
Created on Jun 12, 2017

@author: jwang02
'''
'''
* The list type is a container that holds a number of other objects, in a given order.
  Here the objects can be just about anything. Such as numbers, strings, and so on. 
* The list type implements the sequence protocol, and also allows you to add and remove objects 
  from the sequence.
* Python has no ARRAY data type. List os being used as ARRAY
* To create a list, put a number of expressions in square brackets:

    L = []
    L = [expression, ...]

    
    This construct is known as: list display
      
    Python also supports computed lists, called: list comprehensions
    In its simplest form, a list comprehension has the following syntax:

    L = [expression for variable in sequence]

    where the expression is evaluated once, for every item in the sequence.

    The expressions can be anything; you can put all kinds of objects in lists, including other lists, and multiple references to a single object.

    You can also use the built-in list type object to create lists:

        L = list() # empty list
        L = list(sequence)
        L = list(expression for variable in sequence)

    The sequence can be any kind of sequence object or iterable, including tuples and generators. 
    If you pass in another list, the list function makes a copy.

* Python creates a single new list every time you execute the [] expression. No more, no less. 
  And Python never creates a new list if you assign a list to a variable.

    A = B = [] # both names will point to the same list
 
     A = []
     B = A # both names will point to the same list
 
     A = []; B = [] # independent lists
'''

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for- loop goes through a list
for number in the_count:
    print "This is count %d" % number
    
# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)# now we can print them out too

for i in elements:
    print "Element was: %d" % i