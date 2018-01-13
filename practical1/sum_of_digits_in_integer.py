number = int(input("Enter integer between 0 to 1000: "))
sumofdigits = number % 10 + (number % 100) // 10 + (number % 1000) // 100

if 0 < number < 1000:
    print("The sum of the digits in {0} is {1}.".format(number,sumofdigits))
else:
    print("Error: Number can only be between 0 and 1000.")
          
