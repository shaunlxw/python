n = int(input("Enter number: "))

def display_pattern(n):
    for num2 in range(1,n+1):
        for num in range(num2,1,-1):
            print(num, end = " ")
        print("1")
    
display_pattern(n)
