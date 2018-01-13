#computing vol of cylinder

#input
radius = float(input("Enter radius of cylinder(cm): "))
length = float(input("Enter length of cylinder(cm): "))
pi = 3.14

area = radius * radius * pi
volume = area * length

print("The volume of the cylinder is {0:.0f}cm\u00b3.".format(volume))
