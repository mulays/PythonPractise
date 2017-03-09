L1 = ['Blue','Black', 'White' ,'Orange' ,'Purple', 'Green', 'Pink', 'Navy' , 'Red']
print L1

print L1[1:4]  # Returns ['Black', 'White', 'Orange']

print L1[2:]   # returns ['White', 'Orange', 'Purple', 'Green', 'Pink', 'Navy', 'Red']

print L1[:2]   # returns ['Blue', 'Black']

print L1[-1]   # returns Red

print L1[::-1] # returns reverse list ['Red', 'Navy', 'Pink', 'Green', 'Purple', 'Orange', 'White', 'Black', 'Blue']

print L1[:-1]  # returns all elements except last element  ['Blue', 'Black', 'White', 'Orange', 'Purple', 'Green', 'Pink', 'Navy']

print L1[1:-1] # returns ['Black', 'White', 'Orange', 'Purple', 'Green', 'Pink', 'Navy']

print "Second block"

print len(L1) # return 9

L2 = [8,9,10,1,2,3,89,9,33,2]
print sorted(L2)  # returns [1, 2, 2, 3, 8, 9, 9, 10, 33, 89]

print L2

L2.append(55)  # returns [8, 9, 10, 1, 2, 3, 89, 9, 33, 2, 55]
print L2

L2.insert(0,"999")
print L2      # returns ['999', 8, 9, 10, 1, 2, 3, 89, 9, 33, 2, 55]

# L2.remove(999) will remove 999

del L2[0] # delete by index
print L2  # returns [8, 9, 10, 1, 2, 3, 89, 9, 33, 2, 55]

print L2.pop() # 55 popped
print L2  # returns [8, 9, 10, 1, 2, 3, 89, 9, 33, 2]

print L2.reverse() # this will print None
print L2  # this will return [2, 33, 9, 89, 3, 2, 1, 10, 9, 8]

if 'Red' in L1:
    print "Red in the list"

print type(L1)

print dir(L1)

L3 = [11,11,11]

print L3 * 3 # retuns [4, 5, 6, 4, 5, 6, 4, 5, 6] will print three times the list
#print L3 * L3 # gives an error

print L3.__add__(L2)  # this concatenates the list [11, 11, 11, 2, 33, 9, 89, 3, 2, 1, 10, 9, 8]
print L3  # But the original list remains unchanged


L4 = [11,11,11]
print L3.__contains__(L4) # returns False

print L3.__contains__(11) # returns True

