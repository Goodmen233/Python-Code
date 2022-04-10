import random

# 模拟次数
COUNT = 1000000
# 统计落在每个区域的点数
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
# 假设正方形的边长为2
for i in range(COUNT):
    # 模拟投掷的点
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # 如果落在1区域
    if x < 0:
        sum1 = sum1 + 1
    # 如果落在4区域
    elif y < 0:
        sum4 = sum4 + 1
    # 如果落在3区域
    elif x + y < 1:
        sum3 = sum3 + 1
    # 如果落在2区域
    else:
        sum2 = sum2 + 1
print("飞镖落在奇数区域的概率为：{}".format((sum1 + sum3) / COUNT))