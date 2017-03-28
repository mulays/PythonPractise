#Refer the link https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

def createGen():
    mylist = range(3)
    print mylist
    print "Before For"
    for i in mylist:
        yield i*i+2*8


mygen = createGen()
print "Printing MyGen :"
print mygen

for i in mygen:
    print i

'''
items = [1,2,3,4,5]
squared = []
for x in items:
    squared.append(x ** 2)

print squared
'''
# Using Map
# Refer the link : http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php

items = [1,2,3,4,5]
def square(i):
    return i*i

print list(map(square,items))

print list(map(square, [7, 8, 9]))

print list(range(-5,5))  #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

print list(filter( (lambda x : x < 0),range(-5,5)))  # [-5, -4, -3, -2, -1]

import functools
L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
print functools.reduce( (lambda x,y:x+y), L)



L = [1, 2, 3, 4]
result = L[0]
print L[1:]
for x in L[1:]:    # it means [2,3,4]
	result = result * x
print result  # prints 24

print (reduce( (lambda x, y: x * y), [1, 2, 3, 4,5]))  # print 120

print (map(square, [7, 8, 9])) # prints [49,64,81]
