n = int(input("Enter a number: "))
if n == 1:
    print('1')
else:
    i = 2
    while n >= i: 
        if n%i ==0:
            print(i)
            n = n/i
            i = 2
        else: 
            i = i+1
