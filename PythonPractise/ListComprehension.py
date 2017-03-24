#List comprehension is a complete substitute for the lambda function as well as the functions map(), filter() and reduce()
#"list comprehensions". It can be used to construct lists in a very natural, easy way, like a mathematician is used to do.

l1 = [1,2,3,4,5,6,7,8,9,10]
l1_square = [(x*x) for x in l1]
print "l1_square : ", l1_square

l1_minus5 = [(x-5) for x in l1_square]

print "l1_minus : ",l1_minus5

print "List comprehension : "

#                 1,2,3,4           6,7,8,9           11 12 13 14
l2 = [(x,y,z) for x in range(1,5) for y in range(6,10) for z in range (11,15) if x + y == z]

print "L2 : ",l2

l3 = ["white","black","grey","wine"]
l4 = ["bag","purse","sack"]

l5 = [(x,y) for x in l3 for y in l4]
print "l5 : ",l5

'''
l1_square :  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
l1_minus :  [-4, -1, 4, 11, 20, 31, 44, 59, 76, 95]
List comprehension :
L2 :  [(2, 9, 11), (3, 8, 11), (3, 9, 12), (4, 7, 11), (4, 8, 12), (4, 9, 13)]
l5 :  [('white', 'bag'), ('white', 'purse'), ('white', 'sack'), ('black', 'bag'), ('black', 'purse'), ('black', 'sack'), ('grey', 'bag'), ('grey', 'purse'), ('grey', 'sack'), ('wine', 'bag'), ('wine', 'purse'), ('wine', 'sack')]
>>>
'''

