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

print(max(cal))