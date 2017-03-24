from sets import Set   #Don't forget to add this

managers = Set(['M1','M2','M3','M4','M5'])

managers.add("M_add")
print "Managers : ",managers

cities = frozenset(["Frankfurt", "Basel","Freiburg"])
try :
    cities.add("Pune")

except Exception as e:
    print "You cannot change Frozenset.They are immutable"
    print "Cities : ",cities

#Output
'''
Managers :  Set(['M5', 'M4', 'M1', 'M3', 'M2', 'M_add'])
You cannot change Frozenset.They are immutable
Cities :  frozenset(['Freiburg', 'Basel', 'Frankfurt'])
'''