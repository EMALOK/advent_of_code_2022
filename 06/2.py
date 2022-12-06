from collections import Counter

file = open("data.txt","r")


line = file.readline()


for i in range(0,len(line) - 13):

    sub = line[i:i+14]

    c = Counter(sub)

    (k,v) = c.most_common()[0]

    if v == 1:
        print(c)
        print(i + 14)

