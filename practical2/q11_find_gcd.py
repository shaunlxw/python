n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1 < n2:
    d = n1
    while n2 % d != 0 or n1 % d != 0:
        d -= 1
    print(d)
else:
    d = n2
    while n1 % d != 0 or n2 % d != 0:
        d -= 1
    print(d)
