grid = []

file = open("data.txt","r")

for (y,line) in enumerate(file.read().split("\n")):
    #append new line
    line.strip()

    grid.append([])
    for (x,c) in enumerate(line):
        grid[y].append(int(c))

best_score = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):

        print("--------- new ---------")
        print(x,y)
        #border score = 0 we can skip
        if x == 0 or y == 0 or x == len(grid[y]) - 1 or y == len(grid) - 1:
            continue

        score_up = 0
        score_down = 0
        score_left = 0
        score_right = 0


        # print("up")

        #up
        for yoff in range(y-1,-1,-1):

            # print(yoff,x)

            if grid[yoff][x] < grid[y][x]:
                #tree is smaller
                score_up += 1
            else:
                score_up += 1
                break

        # print("down")

        #down
        for yoff in range(y+1,len(grid),1):

            # print(yoff,x)

            if grid[yoff][x] < grid[y][x]:
                #tree is smaller
                score_down += 1
            else:
                score_down += 1
                break
        
        #print("left")

        #left
        for xoff in range(x-1,-1,-1):

            #print(y,xoff)

            if grid[y][xoff] < grid[y][x]:
                #tree is smaller
                score_left += 1
            else:
                score_left += 1
                break

        # print("right")

        #right
        for xoff in range(x+1,len(grid),1):

            # print(y,xoff)

            if grid[y][xoff] < grid[y][x]:
                #tree is smaller
                score_right += 1
            else:
                score_right += 1
                break

        print("up:",score_up)
        print("down:",score_down)
        print("left:",score_left)
        print("right:",score_right)

        curr_score = score_up * score_down * score_left * score_right
        best_score = max(best_score,curr_score)

print(best_score)