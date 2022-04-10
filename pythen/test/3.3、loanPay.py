rate0 = 5
step = 0.125
totalFor = int((8 - 5) / step)
loanMoney = eval(input("Loan Amount："))
year = eval(input("Number of Years："))
print("{}\t\t{}\t\t{}".format("Interest Rate", "Monthly Payment", "Total Payment"))
for i in range(0, totalFor+1):
    rate = rate0 + i * step
    temp = (1 + rate / 1200)**(year * 12)
    monthlyPayment = (loanMoney * (rate / 1200)) / (1 - 1 / temp)
    totalPayment = monthlyPayment * year * 12
    print("{:.3f}%\t\t\t\t{:.2f}\t\t\t\t{:.2f}".format(rate, monthlyPayment, totalPayment))

