import pprint

grid = []

file = open("data.txt","r")

for (y,line) in enumerate(file.read().split("\n")):
    #append new line
    line.strip()

    grid.append([])
    for (x,c) in enumerate(line):
        grid[y].append(int(c))

count = 0

print(len(grid))
print(len(grid[0]))

for y in range(len(grid)):
    for x in range(len(grid[y])):

        print("--------- new ---------")

        if x == 0 or y == 0 or x == len(grid[y]) - 1 or y == len(grid) - 1:
            count += 1
        else:
            #check directions
            print(y,x)


            visible_up = True
            visible_down = True
            visible_left = True
            visible_right = True

            print("up")

            #up
            for yoff in range(y-1,-1,-1):

                print(yoff,x)

                if grid[yoff][x] >= grid[y][x]:
                    #tree is bigger
                    visible_up = False
                    break

            print("down")

            #down
            for yoff in range(y+1,len(grid),1):

                print(yoff,x)

                if grid[yoff][x] >= grid[y][x]:
                    #tree is bigger
                    visible_down = False
                    break
            
            print("left")

            #left
            for xoff in range(x-1,-1,-1):

                print(y,xoff)

                if grid[y][xoff] >= grid[y][x]:
                    #tree is bigger
                    visible_left = False
                    break

            print("right")

            #right
            for xoff in range(x+1,len(grid),1):

                print(y,xoff)

                if grid[y][xoff] >= grid[y][x]:
                    #tree is bigger
                    visible_right = False
                    break

            if visible_up or visible_down or visible_left or visible_right:
                print("visible")
                count += 1

print(count)
