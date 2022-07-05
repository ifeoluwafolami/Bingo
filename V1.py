# BINGO WITH PYTHON

# 1. Scorecard made of 25 squares
# 2. If you get 5 squares in a row, you win!

###Creating the Score Card
import numpy as np
import random
from tabulate import tabulate

player_card = np.random.randint(1, 100, (5, 5))
player_card = player_card.astype(str) 
player_card[2,2] = 'FREE'
# print(player_card)
print("---------------------------")

bingo_card = [['B', 'I', 'N', 'G', 'O']]
bingo_list = []

bingo = ['B', 'I', 'N', 'G', 'O']

for i in range(0, (len(bingo))):
    numbers = player_card[0:5, i:(i+1)]
    number_list = []
    bingooo = []
    bingooo.append(bingo[i])
    numbers.tolist()
    for number in numbers:
        for no in number:
            number_list.append(no)
    # print(number_list)
    # print("-------------------------")
    bingooo.append(number_list)
    bingo_card.append(number_list)
    bingo_list.append(bingooo)
    
print(tabulate(bingo_card, tablefmt="fancy_grid", stralign="center"))

run = True
#Game Starts, Caller Picks a 'Ball'
# while run: 
#     print("Caller picks a ball!")
#     call_number = np.random.randint(1, 100)
#     call_letter = random.choice(bingo)
#     print("{}-{}".format(call_letter, call_number))

    