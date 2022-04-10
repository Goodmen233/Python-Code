years = int(input("请输入查询的年份： "))
if years % 4 == 0 and years % 100 != 0:
    print(years, "普通闰年")
elif years % 400 == 0:
    print(years, "是世纪闰年")
else:
    print("不是闰年")