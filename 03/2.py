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

upper_b = int(len(lines) / 3)

for i in range(upper_b):

    a = lines[i * 3 + 0].rstrip()
    b = lines[i * 3 + 1].rstrip()
    c = lines[i * 3 + 2].rstrip()

    count_a = Counter(a)
    count_b = Counter(b)
    count_c = Counter(c)

    intersection_abc = count_a & count_b & count_c

    (k,v) = intersection_abc.most_common(1)[0]

    GetScore(k)

print(score)