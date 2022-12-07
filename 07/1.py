import pprint

file = open("data.txt","r")

parsing_ls = False

curr_path = "/"

#(dir_path,cumulative_size)
dir_sizes = dict()

dir_sizes["/"] = 0

def build_path_from_splits(splits):
    temp = "/"

    for curr_split in splits:
        temp += curr_split + "/"

    return temp

for line in file.readlines():
    print("--------- new command ---------")
    print("curr path:",curr_path)

    splits = line.rstrip().split(" ")

    pprint.pprint(splits)

    if splits[0] == "$":
        #command
        if splits[1] == "ls":
            print("ls")
        elif splits[1] == "cd":
            print("cd")
            if splits[2] == "..":
                path_splits = curr_path.split("/")[1:-2] #remove an extra element

                pprint.pprint(path_splits)

                curr_path = build_path_from_splits(path_splits)

            else:
                if splits[2] == "/":
                    curr_path = "/"
                else:
                    curr_path += splits[2] + "/"
    else:
        
        if splits[0] == "dir":

            print("new dir:",curr_path + splits[1] + "/")

            dir_sizes[curr_path + splits[1] + "/"] = 0
        else:

            curr_path_splits = curr_path.split("/")[1:-1]

            for i in range(len(curr_path_splits),-1,-1):
                dir_sizes[build_path_from_splits(curr_path_splits[0:i])] += int(splits[0])
                print(build_path_from_splits(curr_path_splits[0:i]),dir_sizes[build_path_from_splits(curr_path_splits[0:i])])



            

pprint.pprint(dir_sizes)

print("------- done -------")

result = 0

for (k,v) in dir_sizes.items():
    if v <= 100000:
        result += v

print(result)