import random

def print_matrix(n):
    for i in range(n):
        for i in range(n):
            print(random.randint(0,1), end = " ")
        print()

n = int(input("Enter n: "))
print_matrix(n)
