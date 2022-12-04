

file = open("data.txt")


lines = file.readlines()

count = 0

def overlap(s1,e1,s2,e2):

    if e1 >= s2 and e1 <= e2:
        return True

    return False

for line in lines:

    print(line.rstrip())

    parts = line.split(",")



    part1 = parts[0]
    part2 = parts[1]

    part1parts = part1.split("-")
    part2parts = part2.split("-")


    p1s = int(part1parts[0])
    p1e = int(part1parts[1])

    p2s = int(part2parts[0])
    p2e = int(part2parts[1])

    if overlap(p1s,p1e,p2s,p2e) or overlap(p2s,p2e,p1s,p1e):
        print("overlap")
        count += 1



print(count)