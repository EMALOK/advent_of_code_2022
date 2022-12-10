
file = open("data.txt","r")

X = 1
cicle = 1

def cicle_one():

    global cicle

    x_pos = cicle % 40 -1

    if x_pos == X - 1 or x_pos == X or x_pos == X + 1:
        print("#",end="")
    else:
        print(" ",end="")

    if cicle % 40 == 0 and cicle != 0:
        print()

    cicle += 1


def cicle_two():
    print('\033[94m',end="")
    cicle_one()
    cicle_one()
    print('\033[0m',end="")

for line in file.readlines():

    splits = line.split(" ")

    command = splits[0]

    if command == "addx":


        cicle_two()
        X += int(splits[1])
    else:
        cicle_one()
        