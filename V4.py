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

player_card = np.random.randint(1, 75, (5, 5))
player_card = player_card.astype(str) 
player_card[2,2] = 'FREE'
print(player_card)
print("---------------------------")




bingo = ['B', 'I', 'N', 'G', 'O']


bingo_card = []
bingo_groups = []


for i in range(0, 5):
    numbers = player_card[:, i]
    # print(numbers)
    number_list = numbers.tolist()
    number_set = set(number_list)
    number_list.clear()
    run3 = True
    while run3:
        if len(number_set) < 5:
            number_set.add(str(random.randint(1, 75)))
            continue
        else:
            run3 = False
    # print(number_set)


    for number in number_set:
        number_list.append(number)

    # print(number_list)
    random.shuffle(number_list)
    print(number_list)
    
    if i == 2:
        if number_list.index('FREE') != 2:
            swap_value = number_list[2]
            number_list[2] = 'FREE'
            number_list[number_list.index('FREE')] = swap_value
            # print('Swapped!')
            # print(number_list)

    for j in range(0,5):
        player_card[j, i] = number_list[j]

    print("    ")
    print("----------------")




# player_card = np.array(number_set)
# print(player_card)
#     number_list = list(number_set)
    bingo_letter = bingo[i]
    # print(bingo_letter, number_list)
    bingo_groups.append([bingo_letter, number_list])
# print("--------------")
# print(bingo_groups)
    
        
print(tabulate(player_card, headers=bingo, tablefmt="fancy_grid", stralign="center", numalign="center"))
print("---------------------------")

# run = 0
# run2 = 0

# while run <= 60 and run2 <= 20:
#     run += 1
#     print("Caller picks a ball!")
#     call_number = np.random.randint(1, 10)
#     call_letter = random.choice(bingo)
#     print("{}-{}".format(call_letter, call_number))
#     for bingo_group in bingo_groups:
#         if call_letter == bingo_group[0]:
#             number_list = bingo_group[1]
#             for number in number_list:
#                 if number == 'FREE':
#                     pass
#                 elif number == 'X':
#                     pass
#                 elif call_number == int(number):
#                     # print(number)
#                     run2 += 1
#                     row = number_list.index(number)
#                     col = bingo_groups.index(bingo_group)
#                     player_card[row,col] = 'X'
#                     number_list[number_list.index(number)] = 'X'
#                     print("---------------------------")
#                     print(tabulate(player_card, headers=bingo, tablefmt="fancy_grid", stralign="center", numalign="center"))
#                     print("---------------------------")

#                 row0 = []
#                 row1 = []
#                 row2 = []
#                 row3 = []
#                 row4 = []
#                 for i in range(0, 5):
#                     row0.append(bingo_groups[i][1][0])
#                     row1.append(bingo_groups[i][1][1])
#                     row2.append(bingo_groups[i][1][2])
#                     row3.append(bingo_groups[i][1][3])
#                     row4.append(bingo_groups[i][1][4])


#                 # print('----------------------')
#                 # print(row0)
#                 # print(row0.count('X'))
#                 # print(row1)
#                 # print(row1.count('X'))
#                 # print(row2)
#                 # print(row2.count('X'))
#                 # print(row3)
#                 # print(row3.count('X'))
#                 # print(row4)
#                 # print(row4.count('X'))
#                 # print("---------------------------")

# #Determining Bingo!
# # Vertical, done
# #Horizontal, done
# #Diagonal, pending

#                 if bingo_group[0] != 'N' and number_list.count('X') == 5:
#                     print('1: Bingo!')
#                     exit()

#                 elif bingo_group[0] == 'N' and number_list.count('X') == 4:
#                     print("2: Bingo!")
#                     exit()

#                 elif row0.count('X') == 5: 
#                     print('3: Bingo!')
#                     exit()

#                 elif row1.count('X') == 5:
#                     print('4: Bingo!')
#                     exit()

#                 elif row2.count('X') == 4:
#                     print('5: Bingo!')
#                     exit()

#                 elif row3.count('X') == 5:
#                     print('6: Bingo!')
#                     exit()

#                 elif row4.count('X') == 5:
#                     print('7: Bingo!')
#                     exit()