def triangle(a,b,c):
    parameter = a + b + c
    if a + b > c and b + c > a and c + a > b:
        print(parameter)
    else:
        print("Invalid triangle!")

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
triangle(a,b,c)
