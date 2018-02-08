def gcd(m, n):
    if m > n:
        min = n
    else:
        min = m
    
    while m % min != 0 or n % min != 0:
        min -= 1

    return min

# test program
print(gcd(24, 16))
print(gcd(255, 25))

m = int(input("Enter first positive integer: "))
n = int(input("Enter second positive integer: "))

print(gcd(m, n))
