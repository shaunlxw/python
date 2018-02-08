def is_prime(n):
    prime = True
    if n == 2:
        return prime
    elif n < 2:
        prime = False
        return prime
    else: 
        for i in range(2, n):
            if n % i == 0:
                prime = False
    return prime

### hi lao shi
##for i in range(20):
##    if is_prime(i) == True:
##        print(i, end = ' ')
##print("")

count = 1
x = 0
for i in range(100):
    while count <= 10:
        if is_prime(x) == True:
            print(x, end = '\t')
            x += 1
            count += 1
        else:
            x += 1
    else:
        count = 1
        print()

        

n = int(input("Check prime: "))
print(is_prime(n))


