#Geneva Confection

#this problem invloves simply following the instruction
#If the current cart on the mountain is the correct number send
#it into the lake, otherwise see if the current cart on the branch
#can be sent in the lake, if it can send it in. if neither the branch
#or the mountain top have the correct car then send the car from the
#mountain to the branch and repeat the process. Once there are not more carts
#on the mountain and the branch then the recipe has been completed. If there are
# no more carts on the mountain and the art on the branch can't be sent into
# the lake then you cannot complete the recipe

testCase = int(input())
List = []

#Creates a nested list with each test case inside of the main list 'list'

for x in range(testCase):
    List.append([])
    f = input()
    for y in range(int(f)):
        List(x).append(int(input()))

# For each test case

for x in range(testCase):
    #We need to store the location of the ars on the mountain, branch and the are we looking for
    carList = List(x)
    branch = []
    current = 1

    while True:
        #First step:
        #If cars are on the mountain try to sned them into the mountain
        if len(carList) > 0:

            #if the car on the mountain is the one we are looking for sned it to the lake (remove from mountain)
            if carList[-1] == current:
                current