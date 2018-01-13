name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
rate = float(input("Enter hourly pay rate: "))
cpfrate= float(input("Enter CPF contribution rate(%): "))
gross = hours * rate
cpf = gross / 100 * cpfrate
net = gross - cpf

print("Payroll statement for", name)
print("Number of hours worked in week: {0:.0f}".format(hours))
print("Hourly pay rate: ${0:.2f}".format(rate))
print("Gross pay = ${0:.2f}".format(gross))
print("CPF contribution at {0}% = ${1:.2f}".format(cpfrate,cpf))
print("Net pay = ${0:.2f}".format(net))
             
             
              
