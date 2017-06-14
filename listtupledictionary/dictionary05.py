'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
* Sort dictionary items by their values

'''
items = { "coins": 7, "pens": 3, "cups": 2, 
    "bags": 1, "bottles": 4, "books": 5 }
    
for key, value in sorted(items.iteritems(), 
    key=lambda (k,v): (v,k)):
        
    print "%s: %s" % (key, value) 

print "####### #######"    
    
for key, value in sorted(items.iteritems(), 
    key=lambda (k,v): (v,k), reverse=True):
         
    print "%s: %s" % (key, value)  