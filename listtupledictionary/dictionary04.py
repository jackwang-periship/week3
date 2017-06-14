'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
* Test if a key is in a dictionary or not using the keyword in. 
Notice that membership test is for keys only, not for values.
* Using a for loop we can iterate though each key in a dictionary.
* Using built-in sorted() function

'''
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares)

# Output: True
print(2 not in squares)

# membership tests for key only not value
# Output: False
if 49 in squares:
    print "True"
else:
    print "False"

# Iterate
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print "The Key is: ", squares[i]
 
# Add two Python dictionaries     
domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary"}
domains2 = { "us": "United States", "no": "Norway" }

domains.update(domains2)

print domains

items = { "coins": 7, "pens": 3, "cups": 2, 
    "bags": 1, "bottles": 4, "books": 5 }

print    
print "Sort the dictionary based on the keys"    
    
for key in sorted(items.iterkeys()):
    print "%s: %s" % (key, items[key])

print "####### #######"    
    
for key in sorted(items.iterkeys(), reverse=True):
    print "%s: %s" % (key, items[key])




