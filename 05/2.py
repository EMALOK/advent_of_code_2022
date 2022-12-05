import pprint

columns = [[],[],[],[],[],[],[],[],[]]

def move(f,t,a):
    l = len(columns[f])
    columns[t].extend(columns[f][l - a:l])
    for i in range(a):
        columns[f].pop()

file = open("data.txt")

head = True

for line in file.readlines():

    if head:

        if line == "\n":
            head = False
            #reverse the lists
            for ci in range(len(columns)):
                columns[ci].reverse()

            continue

        index = 0
        for i in range(1,35,4):
            if line[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                columns[index].append(line[i])
            index += 1
    else:
        pprint.pprint(columns)

        splits = line.split(" ")

        box_amount = int(splits[1])
        pile_from = int(splits[3]) - 1
        pile_to = int(splits[5]) - 1

        print(box_amount,pile_from,pile_to)
        move(pile_from,pile_to,box_amount)


for iter in columns:
    print(iter[len(iter) - 1],end="")

print()