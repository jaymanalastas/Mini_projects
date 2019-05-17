# make a grid an find out how to movce the dots to the right to make it an s
#lets do the same for 's' its good practice

letter_s = ''
for row in range(7):
    for col in range(7):
        if((row === 0 or row == 3 or row == 6) and col>0 and col<7):