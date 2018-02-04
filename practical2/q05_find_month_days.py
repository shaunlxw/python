x = int(input("Enter year: "))
y = int(input("Enter month in numberical format: "))

if x % 4 == 0 and x % 100 != 0:
    year = "Leap"
elif x % 400 == 0:
    year = "Leap"
else:
    year = "Non-leap"

if y == 4 or y == 6:
        print("30")
elif year == "Leap" and y == 2:
        print("29")
elif year == "Non-leap" and y == 2:
        print("28")
elif y >= 8 and y % 2 == 0:
        print("31")
elif y == 9 or y == 11:
        print("30")
else:
        print("31")



