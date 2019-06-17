class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getPopulation(cls):
        return cls.population
    def isAdult(age):
        return age >= 18

def display(self):
    print(self.name, ' is ', self.age, ' years old')

newPerson = person('tim', 18)

display(newPerson)