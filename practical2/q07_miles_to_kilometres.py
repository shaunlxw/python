print("Miles\tKilometers\tKilometers\tMiles")

for i in range(1,10):
    print("{0}\t{1:.3f}\t\t{2}\t\t{3:.3f}".format(i, (i+1) * 1.609, (i*5+15), (i*5+15)/1.609))
