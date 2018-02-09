def sum_series2(i): 
    a = i / ((2 * i) + 1) 
    if i == 1: 
        return 1 / 3 
    else: 
        return a + sum_series2(i-1)
i = int(input("Enter number: ")) 
print("{0:.3f}".format(sum_series2(i)))
