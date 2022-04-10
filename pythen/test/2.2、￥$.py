rate = eval(input("美元转化为人民币的汇率:"))
method = eval(input("输入0表示美元转换为人民币，1表示人民币转换为美元:"))
if method == 0:
    origin = eval(input("请输入美元："))
    res = origin * rate
    print("{}美元shi是{}元".format(origin, res))
elif method == 1:
    origin = eval(input("请输入人民币："))
    res = round(origin / rate, 2)
    print("{}元shi是{}美元".format(origin, res))
