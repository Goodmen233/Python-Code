import random, time
right = 0
count = 5
beginTime = time.time()
while count > 0:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, num1)
    res = num1 - num2
    res0 = eval(input((str(num1) + "-" + str(num2) + "=")))
    if res0 == res:
        right = right + 1
    count = count - 1
endTime = time.time()
totalTime = round(endTime - beginTime, 2)
print("你本次答对的个数为{},共耗时{}".format(right, totalTime))
