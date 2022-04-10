import random
count = 0
target = random.randint(1, 1000)
while 1:
    try:
        num = eval(input("请输入一个猜测的整数(1至1000):"))
        if num < 1 or num > 1000:
            print("输出的值超出预设范围，不计入猜测次数哦!")
            continue
        elif num > target:
            print("偏大了")
            count = count + 1
        elif num < target:
            print("偏小了")
            count = count + 1
        else:
            print("猜对了")
            count = count + 1
            print("此轮猜测次数是：{}".format(count))
            break
    except :
        print("输入有误，请重试，不计入猜测次数哦")
