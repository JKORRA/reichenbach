import random

#variable that count how many times Moriarty wins
win_moriarty = 0

#total number of rounds
tot = 100000

for _ in range(tot):

    #variable for the sum
    s = 0

    while s <=100:

        holmes = random.randint(1,100) #generate random number
        s = s + holmes #add the random number generated to 's'

    while s <=200:

        moriarty = random.randint(1,100) #generate random number
        s = s + moriarty #add the random number generated to 's'

    if(moriarty > holmes):

        win_moriarty = win_moriarty + 1 #count how many times Moriarty wins

probability_moriarty_wins = win_moriarty/100000
probability_moriarty_wins = probability_moriarty_wins * 100

print(f'The probability of moriarty winning is {probability_moriarty_wins}%')
