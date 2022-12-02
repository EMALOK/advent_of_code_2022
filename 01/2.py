index = 0
cal = []
cal.append(0)

file = open("data.txt","r")

#read line and remove \n

lines = file.readlines()

for line in lines:

    if(line == "\n"):
        index += 1
        cal.append(0)
    else:
        cal[index] += int(line)

#lol
max1 = max(cal)
cal.remove(max1)
max2 = max(cal)
cal.remove(max2)
max3 = max(cal)

print(max1 + max2 + max3)