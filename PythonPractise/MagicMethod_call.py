#http://farmdev.com/src/secrets/magicmethod/
class Test(object):
    def __call__(self, *args, **kwargs):
        print args
        print kwargs
        print '-'*80
print "step 1"
t = Test()
print "step 2"
t(1, 2, 3)
print "step 3"
t(a=1, b=2, c=3)
print "step 4"
t(4, 5, 6, d=4, e=5, f=6)