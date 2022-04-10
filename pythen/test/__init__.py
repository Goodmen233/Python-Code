import datetime
import time

# a = input("请输入")#字符串
# b = eval("1.3 + 4.6")#将字符串转为数字
# c = eval(input("请输入圆的半斤"))#两者结合
#
# a = int(a)
# a *= 6
#
# print("输入的数字*6为：" + str(a))
# print(b)
# print("圆的面积为" + str(c * 3.14 * c))
# #格式化输出
# print("格式化输出{},{},{}".format(1,2,3.13455667))
#增加输出结尾
# print("牛逼",end="=>离谱")

#求输入的三个数的平均值
# first = eval(input("Enter the first number:"))
# second = eval(input("Enter the second number:"))
# third = eval(input("Enter the third number:"))
# a,b,c = eval(input("Input three numbers:"))
# avg = (first + second + third) / 3
# print("{} {} {} 的平均值为=>".format(first, second, third) + str(avg))

# #同步赋值语句
# a, b, c = 1, 2, 4
# #转换值
# a,b = b,a
# print(a,b,c)

# if 0 > 1 :
#     print("Nishi")
# elif 1 > 2 :
#     print("nihao")
# else:
#     print("haha")

# i = 0
# while 10 > i :
#     print("1")
#     i += 1
# print("end")

# a = pow(2,2)#计算2^2
# b = 1.24e-4#科学计数法
# c = 1 + 4j
# r = c.real#获取实部
# i = c.imag#获取虚部
# t = type(a)#获取类型
# print(a,b,c,r,i,t)

#秒换分 秒
#s = eval(input("请输入秒："))
# m = s // 60# 取整
# s = s % 60
# print("{}分{}秒".format(m, s))

#反向输出
# str = input("请输入需要倒置的数:")
# result = str[::-1]
# print(result)

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

time = time.time()
ts = int(time)
cs = ts % 60

tm = ts // 60
cm = tm % 60

th = tm // 60
ch = th % 24

ch += 8# 转为北京时间
if ch >= 24 :
    ch = ch % 24
print("当前时间是{}:{}:{} ".format(ch,cm,cs))



