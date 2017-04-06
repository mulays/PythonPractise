#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html
#http://farmdev.com/src/secrets/magicmethod/
class my_decorator(object):

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()

print "End"