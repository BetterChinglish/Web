import turtle

#画笔设置
turtle.speed(10)
turtle.pensize(8)

#外边框
turtle.penup()
turtle.goto(200,150)
turtle.pendown()
turtle.right(180)
turtle.forward(400)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(300)
turtle.penup()

#内边框
turtle.goto(170,120)
turtle.pendown()
turtle.left(90)
turtle.forward(340)
turtle.left(90)
turtle.forward(240)
turtle.left(90)
turtle.forward(340)
turtle.left(90)
turtle.forward(240)

#眉毛
turtle.penup()
turtle.goto(40,60)
turtle.right(135)
turtle.pendown()


for i in range(10):
    turtle.left(i)
    turtle.forward(10)#右眉毛

turtle.penup()
turtle.goto(-40,60)
turtle.right(135)
turtle.pendown()
for i in range(10):
    turtle.right(i)
    turtle.forward(10)#左眉毛


#嘴巴
turtle.penup()
turtle.goto(0,-20)
turtle.pendown()
turtle.left(90)

for i in range(180):
    turtle.right(1)
    turtle.forward(0.5)#左半边


turtle.penup()
turtle.goto(0,-20)
turtle.pendown()

turtle.right(180)
for i in range(180):
    turtle.left(1)
    turtle.forward(0.5)#右半边

#天线
turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.left(70)
turtle.fd(100)#左
turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.right(115)
turtle.fd(100)#右

#底座
turtle.penup()
turtle.goto(-100,-150)
turtle.pendown()
turtle.right(135)
turtle.circle(10,180)#左

turtle.penup()
turtle.goto(100,-150)
turtle.pendown()
turtle.right(180)
turtle.circle(10,180)#右

turtle.done()
