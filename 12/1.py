import pprint
import copy

file = open("data.txt","r")

grid = []

start = [0,0]
end = [0,0]

for y,line in enumerate(file.readlines()):
    grid.append([])
    line = line.strip()
    for x,c in enumerate(line):
        if c == "S":
            start[0] = x
            start[1] = y
            c = 'a'
        elif c == "E":
            end[0] = x
            end[1] = y
            c = 'z'

        grid[y].append(ord(c) - ord('a'))

queue = []
new_queue = []

print("grid:",len(grid[0]),len(grid))

visited = set([(start[0],start[1])])

queue.append([start[0],start[1],0])
new_queue = queue

time = 0

def check_h(f,t) -> bool:
    return grid[f[1]][f[0]] + 1 >= grid[t[1]][t[0]]

try:

    while len(queue) != 0:

        print("queue",len(queue))
        #print(visited)

        element = queue.pop(0)

        #print("element",element)
        #queue.pop()

        visited.add((element[0],element[1]))

        if element[0] == end[0] and element[1] == end[1]:
            time = element[2]
            raise StopIteration

        candiates = []

        new_counter = element[2] + 1

        if element[0] + 1 < len(grid[0])    and check_h(element,[element[0] + 1,element[1] + 0]):
            candiates.append([element[0] + 1,element[1] + 0,new_counter])

        if element[1] + 1 < len(grid)       and check_h(element,[element[0] + 0,element[1] + 1]):
            candiates.append([element[0] + 0,element[1] + 1,new_counter])

        if element[0] - 1 >= 0              and check_h(element,[element[0] - 1,element[1] + 0]):
            candiates.append([element[0] - 1,element[1] + 0,new_counter])

        if element[1] - 1 >= 0              and check_h(element,[element[0] + 0,element[1] - 1]):
            candiates.append([element[0] + 0,element[1] - 1,new_counter])

        #print("base candidates:",candiates)

        for curr in candiates:
            p = (curr[0],curr[1])

            if p not in visited and curr not in queue:
                #print(p,"not found in set")
                queue.append(curr)
            else:
                #print(p,"in set")
                pass


except StopIteration:
    print("found")

print("end")
print(queue)

print(time)
