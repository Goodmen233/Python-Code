num = input("请输入一个整数：")
sum = 0
for n in num:
   sum += int(n)
print("{}的各个位数之和为=>{}".format(num, sum))