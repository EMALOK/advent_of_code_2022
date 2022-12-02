
score = 0

file = open("data.txt")

lines = file.readlines()

def RPS(you,me) -> int:
    match_result = 0
    my_hand_value = 0

    if me == "X":
        my_hand_value = 1
    if me == "Y":
        my_hand_value = 2
    if me == "Z":
        my_hand_value = 3


    #draw
    if you == "A" and me == "X":
        match_result = 3
    elif you == "B" and me == "Y":
        match_result = 3
    elif you == "C" and me == "Z":
        match_result = 3
    else:
        #not draw
        #win
        if you == "A" and me == "Y":
            #rock - paper
            match_result = 6
        elif you == "B" and me == "Z":
            #paper - scissor
            match_result = 6
        elif you == "C" and me == "X":
            #scissor - rock
            match_result = 6
        else:
            #not win
            match_result = 0

    return match_result + my_hand_value


for line in lines:

    me = line[2]

    you = line[0]

    score += RPS(you,me)

print(score)
