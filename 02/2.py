score = 0

file = open("data.txt")

lines = file.readlines()

def RPS(you,result) -> int:
    match_result = 0
    my_hand_value = 0

    if result == "X":
        #lose
        match_result = 0

        if you == "A":
            my_hand_value = 3
        elif you == "B":
            my_hand_value = 1
        else:
            my_hand_value = 2

    elif result == "Y":
        #draw
        match_result = 3

        if you == "A":
            my_hand_value = 1
        elif you == "B":
            my_hand_value = 2
        else:
            my_hand_value = 3
    else:
        #win
        match_result = 6

        if you == "A":
            my_hand_value = 2
        elif you == "B":
            my_hand_value = 3
        else:
            my_hand_value = 1

    

    return match_result + my_hand_value

for line in lines:

    you = line[0]
    result = line[2]

    score += RPS(you,result)


print(score)