# Printing the Even numbers at the even indexes
l1 = [12,1,24,23,4,1,45,1,66,1,98,1,100]
index = 0

for i in l1:
    if index % 2 == 0:
        if i % 2 == 0:
            print i
        index = index + 1
    else :
        index = index +1

