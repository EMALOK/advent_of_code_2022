
file = open("data.txt","r")

#set di pair
blocked_tiles = set()

point_source = (500,0)

def slidingWindow(sequence,winSize,step=1):
    # Verify the inputs
    if not ((type(winSize) == type(0)) and (type(step) == type(0))):
        raise Exception("**ERROR** type(winSize) and type(step) must be int.")
    if step > winSize:
        raise Exception("**ERROR** step must not be larger than winSize.")
    if winSize > len(sequence):
        raise Exception("**ERROR** winSize must not be larger than sequence length.")

    # Pre-compute number of chunks to emit
    numOfChunks = int((len(sequence)-winSize)/step)+1

    # Do the work
    for i in range(0,numOfChunks*step,step):
        yield sequence[i:i+winSize]


def draw_line(point_from:tuple[int,int],point_to:tuple[int,int]):

    if point_from[0] == point_to[0]:
        
        for i in range(min(point_from[1], point_to[1]),max(point_from[1], point_to[1]) + 1):
            blocked_tiles.add((point_from[0],i))

    elif point_from[1] == point_to[1]:

        for i in range(min(point_from[0], point_to[0]),max(point_from[0], point_to[0]) + 1):
            blocked_tiles.add((i,point_from[1]))

    else:
        raise Exception("**ERROR** draw non orthogonal line.")




for line in file.readlines():

    for old,new in slidingWindow(line.strip().split(" -> "),2):

        old_split = old.split(",")
        new_split = new.split(",")

        old = (int(old_split[0]),int(old_split[1]))
        new = (int(new_split[0]),int(new_split[1]))

        draw_line(old,new)


max_y = 0

for p in blocked_tiles:
    max_y = max(max_y,p[1])

draw_line((-2000,max_y + 2),(2000,max_y + 2))

#false -> è fermo
def simulate(point:tuple[int,int]):

    new_y = point[1] + 1

    #down
    if (point[0],new_y) not in blocked_tiles:
        return (point[0],new_y)
    elif (point[0] - 1,new_y) not in blocked_tiles:
        return (point[0] - 1,new_y)
    elif (point[0] + 1,new_y) not in blocked_tiles:
        return (point[0] + 1,new_y)
    else:
        return False




counter = 0
try:
    while True:

        counter += 1

        print(counter)

        if point_source in blocked_tiles:
            raise StopIteration

        curr = point_source


        #sym loop
        while True:

            #input()
            res = simulate(curr)
            #print(res)

            if res == False:
                #did not move
                blocked_tiles.add(curr)
                break
            else:
                #print(res)
                curr = res
except:
    pass

print(counter - 1)

