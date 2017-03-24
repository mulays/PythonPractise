from sets import Set
engineers = Set(['John','Johny','Janardan','Paplu','Taplu','P2'])
programmers = Set(['P1','P2','P3','P4','P5','Paplu'])
managers = Set(['M1','M2','M3','M4','M5'])
employees = engineers | programmers | managers
print "Employees 1 : ",employees

employees = engineers & programmers
print "Employees 2 : ",employees
print "\n"
print dir(employees)

employees.remove('Paplu')
print "Employees 3 : ",employees


cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))
print "Cities :",cities

try:
    cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
except Exception as e:
    print "In Exception",e


'''
Employees 1 :  Set(['P2', 'Johny', 'P1', 'P4', 'P3', 'Taplu', 'P5', 'M5', 'M4', 'Janardan', 'M3', 'M2', 'M1', 'John', 'Paplu'])
Employees 2 :  Set(['P2', 'Paplu'])


['__and__', '__as_immutable__', '__as_temporarily_immutable__', '__class__', '__cmp__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__sub__', '__subclasshook__', '__xor__', '_binary_sanity_check', '_compute_hash', '_data', '_repr', '_update', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'union_update', 'update']
Employees 3 :  Set(['P2'])
Cities : set([('Paris', 'Berlin', 'London'), ('Python', 'Perl')])
In Exception unhashable type: 'list'
'''
# Sets are implemented in a way, which doesn't allow mutable objects like list
#Though sets can't contain mutable objects, sets are mutable


