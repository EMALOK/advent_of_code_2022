from collections import Counter

def GetScore(inp: str):

    global score

    c = ord(inp[0])

    if(inp[0].isupper()):
        #UPPER
        print(c - ord('A') + 27)
        score += c - ord('A') + 27
    else:
        #lower
        print(c - ord('a') + 1)
        score += c - ord('a') + 1

score = 0

file = open("data.txt","r")

lines = file.readlines()

for line in lines:

    middle = int(len(line) / 2)
    end = len(line)

    comp1 = line[0:middle]
    comp2 = line[middle:end]

    c1 = Counter(comp1)
    c2 = Counter(comp2)

    intersection = c1 & c2

    print(intersection)

    (k,v) = intersection.most_common(1)[0]

    print(k)

    GetScore(k)

print(score)
