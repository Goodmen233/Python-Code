import random
num1 = random.randint(0,9)
num2 = random.randint(0,num1)
res = num1 - num2
res0 = eval(input((str(num1) + "-" + str(num2) + "=")))
if res0 == res:
    print("你答对了")
else :
    print("你的答案是错误的")
    print("正确的答案是：")
    print(str(num1) + "-" + str(num2) + "=" + str(res))