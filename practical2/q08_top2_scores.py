num = int(input("Enter the number of students: "))
x = {}

for i in range(num):
    name = input("Enter name: ")
    score = int(input("Enter {0}'s score: ".format(name)))
    x[score] = name

print(x[max(x)], "has a highest score of", max(x))
x.pop(max(x))
print(x[max(x)], "has a second highest score of", max(x))


