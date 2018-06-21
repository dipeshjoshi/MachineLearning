class Human :

    population = 0

    def __init__(self, gender, name):
        self.gender = gender
        self.name = name
        Human.population += 1

    def die(self):
        print self.name, "is dying...... "
        Human.population -= 1

    def numberOfHuman(self):
        print "current population is : ", self.population




h = Human('M', "Dipesh")
h1 = Human('F', "Fatima")
h2 = Human('M', "Vishal")
Human('M', 'shab')
Human.numberOfHuman
h1.numberOfHuman()
h1.die()
h1.numberOfHuman()
