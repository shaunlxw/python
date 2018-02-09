largest = 0

def find_largest(alist):
    global largest
    if len(alist) == 0:
        return largest
    elif alist[0] > largest:
        largest = alist[0]
        return find_largest(alist[1:])
    else: 
        return find_largest(alist[1:])
    return largest

n = int(input("Enter number of items: ")) 
alist = [] 
for i in range(n): 
    item = int(input("Enter integer: ")) 
    alist.append(item)
print(find_largest(alist))
