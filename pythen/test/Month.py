arr = "JanFebMarAprMayJunJulAugSepOctNovDec"
num = eval(input("请输入月份:"))
print(arr[(num-1)*3:(num*3)])
