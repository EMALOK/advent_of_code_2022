
file = open("data.txt","r")


line = file.readline()


for i in range(0,len(line) - 3):

    a = line[i + 0]
    b = line[i + 1]
    c = line[i + 2]
    d = line[i + 3]
    """
     abcd
    a-xxx
    b -xx
    c  -x
    d   -
    """
    if a != b and a != c and a != d and b != c and b != d and c!= d:
        #all different
        print(a,b,c,d)
        print(i + 3 + 1)
        quit()

