import re

# Refered link : http://www.thegeekstuff.com/2014/07/python-regex-examples
string = "this is my new name \nplate"
stringreg = r"this is my new name \nplate"

print string
print stringreg

re.match(r'dog','dog cat dog mouse dog')
match = re.match(r'cat','dog cat dog mouse dog')
print match

match = re.search(r'cat','dog cat dog cat dog')
print match.group(0)

match = re.findall(r'cat','dog cat dog cat dog')
print match

match = re.search(r'pune', 'dog cat dog cat pune cat cat cat')
print match.start()
print match.end()