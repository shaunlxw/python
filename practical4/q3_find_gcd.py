def gcd(m, n):
    if m % n == 0:
        return n
    elif m < 0 or n < 0:
        print("Error: {0} or {1} is a negative number".format(m, n))
    else:
        return gcd(n, m % n)
    
print(gcd(24, 16))
print(gcd(255, 25))

m = int(input("Enter first integer: "))
n = int(input("Enter second integer: "))

print(gcd(m,n))
