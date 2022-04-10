year,month = eval(input("请输入年和月[以逗号隔开]："))
day = 31
if month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        day = 29
    else:
        day = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    day = 30
print("{}年{}月份有{}天".format(year, month, day))
