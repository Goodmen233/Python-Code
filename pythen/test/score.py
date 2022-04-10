score = eval(input("请输入成绩:"))
if score > 100:
    print("成绩不合法")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 0:
    print("E")
else :
    print("成绩不合法")