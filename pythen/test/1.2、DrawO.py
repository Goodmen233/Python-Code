import turtle
import math

r = eval(input("请输入圆的半径:"))
s = math.pi * r * r
turtle.circle(r)
turtle.penup()
turtle.write(s, font=('Arial', 40, 'normal'))

turtle.done()