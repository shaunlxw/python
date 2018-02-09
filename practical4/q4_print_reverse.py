def reverse_int(n):
    if len(str(n)) == 1:
        print(n)
    else:
        print(n % 10, end = "")
        reverse_int(n // 10)
    
n = int(input("Enter integer: "))
reverse_int(n)
