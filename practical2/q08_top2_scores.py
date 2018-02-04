num = int(input("Enter the number of students: "))
x = {}

for i in range(num):
    name = input("Enter name: ")
    score = int(input("Enter {0}'s score: ".format(name)))
    x[name] = score

keys = sorted(x.items(), key = lambda x: x[1])
print(keys[num-1])
print(keys[num-2])
