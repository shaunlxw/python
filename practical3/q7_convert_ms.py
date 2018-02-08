def convert_ms(n):
    seconds = n // 1000
    minutes = seconds // 60
    hours = minutes // 60
    while seconds >= 60:
        seconds = seconds % 60
    while minutes >= 60:
        minutes = minutes % 60
    print("{0}:{1}:{2}".format(hours,minutes,seconds))

convert_ms(5500)
convert_ms(100000)
convert_ms(555550000)

n = int(input("Enter milliseconds: "))
convert_ms(n)
