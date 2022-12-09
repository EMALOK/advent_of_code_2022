

file = open("data.txt","r")

# (x,y)
# y
# ^
# |
# |
# |
# |
# L--------->x

nodes = [
    [0,0],#H
    [0,0],#1
    [0,0],#2
    [0,0],#3
    [0,0],#4
    [0,0],#5
    [0,0],#6
    [0,0],#7
    [0,0],#8
    [0,0] #9
]

visited_cells = set()

#movees the haed in a given direction
def move_head(direction):
    if direction == "U":
        nodes[0][1] += 1
    elif direction == "D":
        nodes[0][1] -= 1
    elif direction == "L":
        nodes[0][0] -= 1
    else:
        nodes[0][0] += 1

#check if node[index_1] is near node[index_2]
def near(index_1,index_2):
    if nodes[index_1][0] >= nodes[index_2][0] - 1 and nodes[index_1][0] <= nodes[index_2][0] + 1 and nodes[index_1][1] >= nodes[index_2][1] - 1 and nodes[index_1][1] <= nodes[index_2][1] + 1:
        return True
    return False

# node_index is ge 1
def move_node(node_index):

    if not near(node_index,node_index-1):

        diff = [nodes[node_index - 1][0] - nodes[node_index][0],nodes[node_index - 1][1] - nodes[node_index][1]]

        if diff[0] != 0:
            diff[0] = diff[0] / abs(diff[0])
        
        if diff[1] != 0:
            diff[1] = diff[1] / abs(diff[1])

        nodes[node_index] = [nodes[node_index][0] + diff[0],nodes[node_index][1] + diff[1]]


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

        for i in range(1,len(nodes)):
            move_node(i)

        last = nodes[len(nodes) - 1]
        visited_cells.add((last[0],last[1]))

visited_cells.add((0,0))

print(len(visited_cells))