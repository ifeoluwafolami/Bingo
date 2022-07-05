# BINGO WITH PYTHON

# 1. Scorecard made of 25 squares
# 2. If you get 5 squares in a row, you win!


###Creating the Score Card
import numpy as np
import random
from tabulate import tabulate

player_card = np.zeros((5,5))
player_card = player_card.astype(str) 
player_card[2,2] = 'FREE'
# print(player_card)
# print("---------------------------")

B = []
I = []
N = []
G = []
O = []


bingo = ['B', 'I', 'N', 'G', 'O']

bingo_list = [B, I, N, G, O]

bingo_card = []
bingo_groups = []

def number_gen(i):
    match i:
        case 0:
            numbers = np.random.randint(1, 15, 5)
        case 1:
            numbers = np.random.randint(16, 30, 5)
        case 2:
            numbers = np.random.randint(31, 45, 5)
        case 3:
            numbers = np.random.randint(46, 60, 5)
        case 4:
            numbers = np.random.randint(61, 75, 5)
    return numbers
    
def extra_number_gen(i):
    match i:
        case 0:
            number_set.add(str(random.randint(1, 15)))
        case 1:
            number_set.add(str(random.randint(16, 30)))
        case 2:
            number_set.add(str(random.randint(31, 45)))
        case 3:
            number_set.add(str(random.randint(46, 60)))
        case 4:
            number_set.add(str(random.randint(61, 75)))



for i in range(0, 5):
    numbers = number_gen(i)
    numbers = numbers.astype(str)
    number_list = numbers.tolist()
    number_set = set(number_list)
    number_list.clear()
    run3 = True
    while run3:
        if len(number_set) < 5:
            extra_number_gen(i)
            continue
        else:
            run3 = False
    # print(number_set)


    for number in number_set:
        number_list.append(number)

    # print(number_list)
    random.shuffle(number_list)
    # print(number_list)
    
    if i == 2:
        number_list[2] = 'FREE'
        # print(number_list)

    for j in range(0,5):
        player_card[j, i] = number_list[j]

    # print("    ")
    # print("----------------")




# player_card = np.array(number_set)
# print(player_card)
#     number_list = list(number_set)
    bingo_letter = bingo[i]
    # print(bingo_letter, number_list)
    bingo_groups.append([bingo_letter, number_list])
# print("----BINGO GROUPS----------")
# print(bingo_groups)
    
        
print(tabulate(player_card, headers=bingo, tablefmt="fancy_grid", stralign="center", numalign="center"))
print("---------------------------")

run = 0
run2 = 0

while run <= 100 and run2 <= 23:
    run += 1
    print("Caller picks a ball!")
    
    call_letter = random.choice(bingo)

    match call_letter:
        case 'B':
            call_number = np.random.randint(1, 15)
        
        case 'I':
            call_number = np.random.randint(16, 30)

        case 'N':
            call_number = np.random.randint(31, 45)

        case 'G':
            call_number = np.random.randint(46, 60)

        case 'O':
            call_number = np.random.randint(61, 75)


    print("{}-{}".format(call_letter, call_number))
    for bingo_group in bingo_groups:
        if call_letter == bingo_group[0]:
            number_list = bingo_group[1]
            for number in number_list:
                if number == 'FREE':
                    pass
                elif number == 'X':
                    pass
                elif call_number == int(number):
                    # print(number)
                    run2 += 1
                    row = number_list.index(number)
                    col = bingo_groups.index(bingo_group)
                    player_card[row,col] = 'X'
                    number_list[number_list.index(number)] = 'X'
                    print("---------------------------")
                    print(tabulate(player_card, headers=bingo, tablefmt="fancy_grid", stralign="center", numalign="center"))
                    print("---------------------------")

                row0 = []
                row1 = []
                row2 = []
                row3 = []
                row4 = []
                diag1 = []
                diag2 = []

                for i in range(0, 5):
                    row0.append(bingo_groups[i][1][0])
                    row1.append(bingo_groups[i][1][1])
                    row2.append(bingo_groups[i][1][2])
                    row3.append(bingo_groups[i][1][3])
                    row4.append(bingo_groups[i][1][4])
                    diag1.append(bingo_groups[i][1][i])
                    diag2.append(bingo_groups[4-i][1][i])

                # print('----------------------')
                # print(row0)
                # print(row0.count('X'))
                # print(row1)
                # print(row1.count('X'))
                # print(row2)
                # print(row2.count('X'))
                # print(row3)
                # print(row3.count('X'))
                # print(row4)
                # print(row4.count('X'))
                # print("---------------------------")

#Determining Bingo!
# Vertical, done
#Horizontal, done
#Diagonal, pending

                if bingo_group[0] != 'N' and number_list.count('X') == 5:
                    print('1: Bingo!')
                    exit()

                elif bingo_group[0] == 'N' and number_list.count('X') == 4:
                    print("2: Bingo!")
                    exit()

                elif row0.count('X') == 5: 
                    print('3: Bingo!')
                    exit()

                elif row1.count('X') == 5:
                    print('4: Bingo!')
                    exit()

                elif row2.count('X') == 4:
                    print('5: Bingo!')
                    exit()

                elif row3.count('X') == 5:
                    print('6: Bingo!')
                    exit()

                elif row4.count('X') == 5:
                    print('7: Bingo!')
                    exit()

                elif diag1.count('X') == 4:
                    print('8: Bingo!')
                    exit()
                
                elif diag2.count('X') == 4:
                    print('9: Bingo!')
                    exit()