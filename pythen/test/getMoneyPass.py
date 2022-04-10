import sys
count = 0
maxTry = 3
password = "123456"
while count < maxTry:
    password0 = input("请输入取款密码:")
    if password == password0:
        print("密码输入正确，正式进入系统！")
        sys.exit()
    else:
        count = count + 1
        print("密码输入错误，你已经输入{}次".format(count))
print("密码已经错误{}次，请和发卡行联系".format(maxTry))
