# __init__ : In python this function is same as constructor in java. This method runs as soon as object of class is being instantiated.

class Animal:
    def __init__(self):
        self.category = "Dog"

    def printInfo(self):
        print "Hello There, I am a : ", self.category


a = Animal()
a.printInfo()
