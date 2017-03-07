#import xml.etree.ElementTree as ET
#fh1 = open('C:\\Snehal\\sample.xml', 'r+')
#fh1.write(data)
#fh1.read()
#print "In for", fh1

#for line in fh1:
#    print line,
#    tree = ET.parse(fh1)
#    root = tree.getroot()
#    for child in root:
#         if "rank" in child.tag:
#             d1 = child.attrib
#             print d1
#    if d1['period'] == "300":
#        self.log.info("Updated value 300 present")
#    else:
#        return False


#tree = ET.parse('C:\\Snehal\\sample.xml')
#root = tree.getroot()
#print root
'''
fh1 = open('C:\\Snehal\\sample.xml', 'r+')
data = fh1.read()
#print  data
print type(data)
fh1.close()

fh2 = open('C:\\Snehal\\sampleNew.xml', 'w+')
fh2.write(data)


fh2.close()
fh3 = open('C:\\Snehal\\sampleNew.xml', 'r+')
data = fh3.read()
print  data
fh3.close()
print "READ LINE"
fh4 = open('C:\\Snehal\\sampleNew.xml','r+')
data4 = fh4.readlines()
print data4
fh4.close()
'''
import os

#handle1 = open('C:\\Snehal\\test.txt','w+')
#data = handle1.readlines()
#handle1.write("THIS IS END OF THE FILE")
#print handle1.read()
#handle1.close()
#print data

with open('C:\\Snehal\\test.txt','a+') as t1:
    t1.write("NEW LINE ADDED")


# Interview Questions :
t1 = open('C:\\Snehal\\test.txt','r+')

data = t1.read()
data = data.split() # this will give the list of all the words
print data

# Count number of occurences of a letter f
for word in data:
    if word.count('f') >= 3:
        print word

# Count number of occurences of each word
dataCount = {}
for word in data:
    try:
        dataCount.update({word : dataCount[word]+1})
    except:
        dataCount.update({word :1})
print dataCount
t1.close()






















