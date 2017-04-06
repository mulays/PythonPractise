str1 = "Snehal Mulay"

print str1[::-1]

l = len(str1)

rev = []
while l:
    l = l - 1
    rev.append(str1[l])

print rev


rev1 = ""
l = len(str1)
while l:
    l = l -1
    rev1 = rev1 + str1[l]

print rev1
