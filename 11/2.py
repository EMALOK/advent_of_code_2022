import pprint
from tqdm import tqdm

file = open("data.txt","r")

lines = file.readlines()

monkeys = []
monkey_index = 0

super_modulo = 1

monkey_businnes = []

def print_items():
    for curr in monkeys:
        print(curr["items"])

for line in lines:
    line = line.strip()

    if line == "":
        monkey_index += 1
        print("new monkey",monkey_index)
    else:
        
        splits = line.split(" ")

        if splits[0] == "Monkey":

            monkeys.append(dict())
            monkey_businnes.append(0)

        elif splits[0] == "Starting":
            
            numbers = splits[2:]

            for (i,num) in enumerate(numbers):
                
                if i != len(numbers) - 1:
                    numbers[i] = num[:-1]

            for (i,num) in enumerate(numbers):
                numbers[i] = int(num)

            monkeys[monkey_index]["items"] = numbers

        elif splits[0] == "Operation:":

            monkeys[monkey_index]["operation"] = compile(line.split(":")[1].strip().split("=")[1].strip(),"","eval",optimize=2)

        elif splits[0] == "Test:":
            super_modulo *= int(splits[3])
            monkeys[monkey_index]["test"] = int(splits[3])

        elif splits[0] == "If":

            monkeys[monkey_index][splits[1][:-1]] = int(splits[5])

pprint.pprint(monkeys)


for round in tqdm(range(1,10001)):

    #print("new round")

    for (i,curr_monkey) in enumerate(monkeys):

        #print("new monkey")


        for curr_item in tqdm(curr_monkey["items"],leave=False):

            monkey_businnes[i] += 1

            old = curr_item

            #print("old",old)
            #print("operation",curr_monkey["operation"])
            new = eval(curr_monkey["operation"]) % super_modulo

            #thanks python
            #new = new // 3

            #print("worry level",new)

            #print_items()
            
            if new % curr_monkey["test"] == 0:
                #true
                monkeys[curr_monkey["true"]]["items"].append(new)
            else:
                #false
                monkeys[curr_monkey["false"]]["items"].append(new)
        curr_monkey["items"].clear()
                
    #print()
    #print_items()

print(monkey_businnes)

max1 = max(monkey_businnes)
monkey_businnes.remove(max1)
max2 = max(monkey_businnes)

print(max1 * max2)