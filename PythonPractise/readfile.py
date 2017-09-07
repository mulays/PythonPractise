fd = open("test","r")
data = fd.read()
print data

words = data.split()
print len(words)
d = {}
for i in words:
    if i in d:
        d[i] = d[i] +1
    else:
        d[i] = 1

print d

