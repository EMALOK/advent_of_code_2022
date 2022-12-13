from functools import cmp_to_key
import pprint

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

                tmp = [left[i]]

                res = right_order(tmp,right[i])

                if res == cant_decide:
                    continue
                else:
                    return res

        if type(left[i]) == list:
            
            if type(right[i]) == list:

                res = right_order(left[i],right[i])

                if res == cant_decide:
                    continue
                else:
                    return res

            elif type(right[i]) == int:
                tmp = [right[i]]

                res = right_order(left[i],tmp)

                if res == cant_decide:
                    continue
                else:
                    return res
    
    if len(left) == len(right):
        return cant_decide
    #if left is shorter return true
    #else return false
    return len(left) < len(right)

def compare(item1, item2):
    res = right_order(item1,item2)

    if res:
        return 0
    else:
        return -1

packets = []

for i,pair in enumerate(file.read().replace("\n\n","\n").split("\n")):

    packets.append(eval(pair))

packets.append([[2]])
packets.append([[6]])

packets.sort(key=cmp_to_key(compare),reverse=True)

pprint.pprint(packets)

a = packets.index([[2]]) + 1
b = packets.index([[6]]) + 1


print(a * b)