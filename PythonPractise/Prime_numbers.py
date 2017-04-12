S = [1,2,3,4,5,6,7,8,9,10]

V = [x*2 for x in S]

print V


#prime_list = [x for x in range(5, 50) for y in range(2,x) if x % x == 0 and x % 1 == 0 and x % y != 0]
#print prime_list


N = 40
print [p for p in range(2,N) if 0 not in [p%d for d in range(2,p/2)]]

L1 = [3,5,7,8,9,10,11,13,15,17,0,0,67,0,0,0]
S1 = [0,0,0,0,1]
S2 = [3,3,3]

print [x for x in S2 if 0 not in S2]

print "TEST PROGRAM"
N = 10
print [p for p in range(2,N) if 0 in [p%d for d in range(2,p)]]




'''
Output :

>>>
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
[3, 3, 3]
TEST PROGRAM
[4, 6, 8, 9]
>>>
'''
