import xml.etree.ElementTree as ET
import os

fh1 = open('C:\\Snehal\\test.xml','r+')
data = fh1.read()

#print data

tree = ET.fromstring(data)
print tree
print "PRINTING TYPE : ",type(tree)

for i in tree:
    print "Printing I : ",i
    print "printing SPLIT : ",i.tag.split("}")
    if i.tag.split("}")[1] == 'input':
        print i.attrib.get('period')

s = "abctdedejdAhejhed}sjdkjksdf{jahjd}"
print s.split("}",2)

print s.strip("}")

fh1.close()

fh2 = open('C:\\Snehal\\priti.txt','r')
data1 = fh2.read()
data1 = data1.split()
#print data1

mydiction = {}

for i in data1:
    try:
        mydiction.update({i : mydiction[i]+1})

    except:
        mydiction.update({i : 1})

print mydiction


l1 = [3,3,3]
l2 = [5,5,5,8,9,7,3]
A = range(10)
print A

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print A0

print sorted(l2)

for i in l2:
    print i*2


print "HANDLING EXCEPTION\n"
i = 6

try:
    if i==6:
        print "Value ",i/0
except:
    print "Something went wrong"

finally:
    print "end of the program"

import json
path = open("C:\\Snehal\priti.txt")
#print open(path).readline()
line = path.read()
records = json.loads(line)
#print dir(records)

print records,type(records)
print line,type(line)

l1 =  records["tags"]
l1.append("new thing")
print l1

print "THIS IS FOR XML FILE"
path = open("C:\\Snehal\\test.xml")
line = path.read()
#records = json.loads(line)
#print records

l1 = ['aa','aa','bb','cc','dd','aa','dd','cc']
counts = {}
for i in l1:
    if i in counts:
        print "I :",counts[i]
        counts[i] = counts[i] + 1
    else :
        counts[i] = 1

print counts


# from the book
from collections import defaultdict
cnt = defaultdict(int)
print cnt
for x in l1:
    cnt[x] = cnt[x] + 1

print cnt

from collections import Counter
print "Counter :",Counter(l1)

import re
str1 = "{snehal{abc}}mulay{pqr{{op{pune}{calsoft}}"
newlist = []
for i in str1:
    newlist.append(i)

print newlist
#aList = [123, 'xyz', 'zara', 'abc'];
#print "A List : ", aList.pop()
#print "B List : ", aList.pop(2)
#print aList

'''
w = len(newlist)
i = 0
for i < w:
    c = newlist.pop
    if c == '}':
        count1 = count1 + 1
        go to for
    if c == '{':


    else :
        append the string
w++
'''

print l1


l2 = [3,4,34,4,23,67,78,99,34,22]
print l2
l2.sort()
print l2
print l2[::-1]

str3 = "snehalabceded5656"


regex = "[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12, 1234, 3456")

print matches

for match in matches:
    print "% s" % (match)

string = "this is my new name \nplate"
stringreg = r"this is my new name \nplate"

print string
print stringreg
























