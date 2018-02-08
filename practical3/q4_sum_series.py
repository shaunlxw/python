def m_series(i):
    a = i / (i + 1)
    if i == 1:
        return a
    else:
        return a + m_series(i-1)

def main(i):
    print("i" "\t", "m(i)")
    x = m_series(i)
    for num in range(1,i+1):
        print("{0}\t{1:.4f}".format(num, m_series(num)))

main(20)
    
i = int(input("Enter integer: "))

main(i)



