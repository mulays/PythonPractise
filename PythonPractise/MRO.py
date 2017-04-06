class A(object):
    def who(self):
        print "In A"
        print self

class B(A):
#    def who(self):
#        print "In B"
     pass
class C(A):
#    def who(self):
#        print "In C"
    pass
class D(B,C):
#    def who(self):
#        print "In D"
     pass
d1 = D()
d1.who()
# Method of D will be called if not commented, if you comment that method then method from B will be called means whichever first in the bracket derived
# if that is also commented then method of A will be called
