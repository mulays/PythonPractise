
l1 = [2,3,4,5]

try :
    print l1['apples']

except TypeError as e:
    print "Type Error Exception", e
#    raise e   # if it is uncommented then it will raise it saying "Type Error Exception list indices must be integers, not str" and after it only finally block will be executed

except Exception as e:
    print "In exception",e

else :    # the code in the else-block executes if the code in the try: block does not raise an exception.
    print "End of program"
    l2 = [8,8,8,8]
    print l2

finally :
    print "In finally" # even if the exception is "raised" ,it will get executed


l3 = [3,4]
print l3   # if exception is "raised" , this will not get executed , if it is not raised then this will be executed