# BINGO WITH PYTHON

# 1. Scorecard made of 25 squares
# 2. If you get 5 squares in a row, you win!

#####################     TO DO LIST    #############################
# Make sure numbers in same column are not identical
# Make sure the caller does not repeat combinations. Create a list of random combinations, then convert to set to obtain unique elements, 
#then use random choice to call combos from that set.

###Creating the Score Card
from tracemalloc import stop
import numpy as np
import random
from tabulate import tabulate

player_card = np.random.randint(1, 10, (5, 5))
player_card = player_card.astype(str) 
player_card[2,2] = 'FREE'
# print(player_card)
print("---------------------------")

B = []
I = []
N = []
G = []
O = []


bingo = ['B', 'I', 'N', 'G', 'O']
bingo_numbers = [B, I, N, G, O]

bingo_card = []
bingo_groups = []


for i in range(0, 5):
    numbers = player_card[:, i]
    # print(numbers)
    number_list = numbers.tolist()
    bingo_letter = bingo[i]
    # print(bingo_letter, number_list)
    bingo_groups.append([bingo_letter, number_list])
# print("--------------")
# print(bingo_groups)
    
        
print(tabulate(player_card, headers=bingo, tablefmt="fancy_grid", stralign="center", numalign="center"))
print("---------------------------")

run = 0
run2 = 0

while run <= 50 and run2 <= 10:
    run += 1
    print("Caller picks a ball!")
    call_number = np.random.randint(1, 10)
    call_letter = random.choice(bingo)
    print("{}-{}".format(call_letter, call_number))
    for bingo_group in bingo_groups:
        if call_letter == bingo_group[0]:
            number_list = bingo_group[1]
            for number in number_list:
                if number == 'FREE':
                    pass
                elif call_number == int(number):
                    # print(number)
                    run2 += 1
                    row = number_list.index(number)
                    col = bingo_groups.index(bingo_group)
                    player_card[row,col] = 'X'
                    print("---------------------------")
                    print(tabulate(player_card, headers=bingo, tablefmt="fancy_grid", stralign="center", numalign="center"))
                    print("---------------------------")
                    break