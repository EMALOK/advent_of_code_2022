

file = open("data.txt","r")

# (x,y)
# y
# ^
# |
# |
# |
# |
# L--------->x
head = [0,0]
tail = [0,0]

visited_cells = set()

#movees the haed in a given direction
def move_head(direction):
    if direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1
    elif direction == "L":
        head[0] -= 1
    else:
        head[0] += 1

#check if the tail is near the head
def near():
    if head[0] >= tail[0] - 1 and head[0] <= tail[0] + 1 and head[1] >= tail[1] - 1 and head[1] <= tail[1] + 1:
        return True

    return False


def move_tail():
    global tail

    if not near():

        diff = [head[0] - tail[0],head[1] - tail[1]]

        if diff[0] != 0:
            diff[0] = diff[0] / abs(diff[0])
        
        if diff[1] != 0:
            diff[1] = diff[1] / abs(diff[1])

        tail = [tail[0] + diff[0],tail[1] + diff[1]]


visited_cells.add((0,0))

for command in file.readlines():

    command_split = command.split(" ")

    direction = command_split[0]
    movement_amount = int(command_split[1])

    for i in range(movement_amount):

        print()
        print(direction)

        #input()

        move_head(direction)
        move_tail()

        visited_cells.add((tail[0],tail[1]))

        print("H",head)
        print("T",tail)

visited_cells.add((0,0))

print(len(visited_cells))