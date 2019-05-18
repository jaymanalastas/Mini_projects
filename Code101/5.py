# create a class that has 2 methods

# 1. getString: grab string from input
# 2. printString: print that string in upper case

class Mama(object):
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input('Give me a string: ')
    def printString(self):
        print(self.s.upper())

x = Mama()
print(x)

#calling a class will print out Mama memory location
#if i want to actually execute functions from class. I need to call it
x.getString()
x.printString()