import calendar

# 缓存每月的天数,根据是否是闰年
leapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
noLeapYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 判断是否为闰年
def isr(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return 1

# 输出日历
def show(year, whichDayOfTheWeek, DayOfMonth):
    for i in range(12):
        print()
        print("                ", calendar.month_name[i + 1], year, "           ")
        print("---------------------------------------------------")
        print("Sun\t\tMon\t\tTue\t\tWed\t\tThu\t\tFri\t\tSat")
        # 用来缓存每个月的天数
        days = []
        for j in range(1, DayOfMonth[i] + 1):
            days.append(j)
        # 为打印该年的第一天留空
        print("\t\t"*(whichDayOfTheWeek % 7), end='')
        temp = 0
        while temp < len(days):
            if whichDayOfTheWeek <= 6:
                print(days[temp], "\t\t", end='')
                temp += 1
                whichDayOfTheWeek += 1
            else:
                print()
                whichDayOfTheWeek = 0
                print()

year = eval(input("请输入年份:"))
whichDayOfTheWeek = eval(input("请输入该年份第一天是星期几:"))
if isr(year):
    show(year, whichDayOfTheWeek, leapYear)
else:
    show(year, whichDayOfTheWeek, noLeapYear)
