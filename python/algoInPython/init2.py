#Passing arguments while creating object of class.

class Animal:

    def __init__(self, category, name):
        self.category = category
        self.name = name

    def printInfo(self):
        print "Hello There, I am a : ", self.category ,". And my name is : ", self.name


a = Animal('Lion', 'Simba')
a.printInfo()
