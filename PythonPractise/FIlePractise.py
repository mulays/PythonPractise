import xml.etree.ElementTree as ET

fh1 = open('C:\\Snehal\\test.xml', 'r+')
data = fh1.read()
print "TYPE OF DATA :",type(data)
tree = ET.fromstring(data)
print "TYPE OF TREE",type(tree)
print "DIR OF TREE : ",dir(tree)
#print "TEXT of TREE ", , "END "
for i in tree:
    print dir(i)

    print i.tag
    print i.text
    if i.tag.split("}")[1] == 'input':
        if int(i.attrib.get('period')) == 300:
            print "In if", i.attrib
        else:
            print "In else"