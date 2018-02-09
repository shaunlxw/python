def sum_digits(n):
    if len(str(n)) == 1:
        return n
    else: 
        return (n % 10) + sum_digits(n // 10)
    
n = int(input("Enter number: "))
print(sum_digits(n))
