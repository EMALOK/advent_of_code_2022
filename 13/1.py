

file = open("data.txt","r")

cant_decide = 59846598275827928

def right_order(left,right):

    size = min(len(left),len(right))

    for i in range(size):
        
        if type(left[i]) == int:
            
            if type(right[i]) == int:

                if left[i] == right[i]:
                    continue
                else:

                    if left[i] < right[i]:
                        return True
                    else:
                        return False

            elif type(right[i]) == list:

                left[i] = [left[i]]

        if type(left[i]) == list:
            
            if type(right[i]) == list:

                res = right_order(left[i],right[i])

                if res == cant_decide:
                    continue
                else:
                    return res

            elif type(right[i]) == int:
                right[i] = [right[i]]

                res = right_order(left[i],right[i])

                if res == cant_decide:
                    continue
                else:
                    return res
    
    if len(left) == len(right):
        return cant_decide
    #if left is shorter return true
    #else return false
    return len(left) < len(right)

count = 0

for i,pair in enumerate(file.read().split("\n\n")):

    splits = pair.split("\n")

    left = eval(splits[0])
    right = eval(splits[1])

    print(left)
    print(right)

    print(right_order(left,right))

    if right_order(left,right):
        count += i + 1


print(count)