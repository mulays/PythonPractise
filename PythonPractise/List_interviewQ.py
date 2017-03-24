# all the 0's should be on left side and all the 1's should be on right side

L1 = [0,0,0,0,1,0,0,1,1,0,0,0,0,0]

for i in L1:
    if i == 1:
        L1.remove(i)
        L1.append(i)

print L1
# gives output [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]