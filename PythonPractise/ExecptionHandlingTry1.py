def C():
    L1 = [2,3,4]
    print "In C"
    try:
        print L1("snehal")
    except Exception as e:
        print"Exception Block : ",e

def B():
    print "In B"
    C()

def A():
    print "In A"
    B()

A()

print "Program completed"

'''Output is :
In A
In B
In C
Exception Block :  'list' object is not callable
Program completed

if try catch is not written , it will only print  In A , In B and it will error out
'''
