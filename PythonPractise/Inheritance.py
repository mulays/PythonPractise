
class Car:
    model = "basic"
    __secretvar = 99
    def __init__(self):
        steering ="basic"
        gearing = "manual"
        print "Instance of basic car created :",steering,gearing
    def getColor(self):
        print "Color is white"
    def displayCar(self):
        print "This is basic car"
        print "This is private variable of class car" ,self.__secretvar
        print "where 1 "

class SUV(Car):
    model ="evo"
    def __init__(self):
        steeing = "advanced"
        gearing = "auto"
        print "Instance of punto created :",steeing,gearing

    def setColor(self,color):
        self.color = color
        print "Color :",color

    def getColor(self):
        print "Color of SUV",self.color

    def displayCar(self):
        print "this is premium car"

print "Creating SUV instance"
myCar = SUV()
myCar.displayCar()
myCar.setColor("wine")
myCar.getColor()
myCar.displayCar()
print myCar.model
print "Creating Base Car instance"
basicCar = Car()
print Car.model
basicCar.displayCar()
print "Where?"
print basicCar._Car__secretvar #underscore Class name double underscore variable name  Obj._Class__var
#print Car.__secretvar

print "Split the output"
print myCar.__init__
'''
if issubclass(punto,Car):
    print "Punto is subclass of Car"

if isinstance(myCar,Car):
    print "myCar is instance of punto "

'''


*** Remote Interpreter Reinitialized  ***
>>>
Creating SUV instance
Instance of punto created : advanced auto
this is premium car
Color : wine
Color of SUV wine
this is premium car
evo
Creating Base Car instance
Instance of basic car created : basic manual
basic
This is basci car
This is private variable of class car 99
where 1
Where?
99
Split the output
<bound method SUV.__init__ of <__main__.SUV instance at 0x03817080>>
>>>
