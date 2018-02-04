x = int(input("Enter year: "))

if x % 4 == 0 and x % 100 != 0:
    year = "Leap"
elif x % 400 == 0:
    year = "Leap"
else:
    year = "Non-leap"

if year == "Leap":
    print(year)
else:
    print(year)


