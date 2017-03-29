class CustomValueError(ValueError):
 def __init__(self, arg):
  self.strerror = arg
  self.args = {arg}
  print "SELF-ERROR : ",self.strerror
  print "SELF-ARG : ",self.args

try:
    obj01 = CustomValueError("Value must be within 1 and 10.")
    print "obj01: ", id(obj01)
    raise obj01


except CustomValueError as e:
    print "e: ", id(e)
    print("CustomValueError Exception!", e.strerror)


#Output
#SELF-ERROR :  Value must be within 1 and 10.
#SELF-ARG :  ('Value must be within 1 and 10.',)
#obj01:  62570288
#e:  62570288
#('CustomValueError Exception!', 'Value must be within 1 and 10.')
