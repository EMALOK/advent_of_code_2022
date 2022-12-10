
file = open("data.txt","r")

result = 0
cicle = 0
X = 1

def cicle_one():

    global cicle
    global result

    cicle += 1
    if (cicle - 20) % 40 == 0:
        result += cicle * X
        print("step",cicle,"add",cicle * X,"res",result)

def cicle_two():
    cicle_one()
    cicle_one()

for line in file.readlines():

    splits = line.split(" ")

    command = splits[0]

    if command == "addx":
        cicle_two()
        X += int(splits[1])
    else:
        cicle_one()

print(result)