username = "admin"
password = "123456"
username0 = input("请输入用户名：")
if username0 == username :
    password0 = input("请输入密码：")
    if password0 == password :
        print("密码正确，恭喜进入")
    else:
        print("密码错误，请重新输入")
else:
    print("用户名有误，请重新输入！")
