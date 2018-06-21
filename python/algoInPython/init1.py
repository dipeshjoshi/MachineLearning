# What ever is to be passed in arguments but its always going to set animals category dog and its name frudo.


class Animal:

    def __init__(self, name):
        self.category = "Dog"
        self.name = "Frudo"

    def printInfo(self):
        print "Hello There, I am a : ", self.category, ". And my name is : ", self.name


a = Animal("prada")
a.printInfo()
