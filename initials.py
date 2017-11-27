import turtle
import math
window = turtle.Screen()
window.bgcolor = ("white")
seth = turtle.Turtle()
seth.pencolor("blue")
seth.shape("turtle")
seth.color("blue")
l = 100
#œ»–¥L
seth.seth(90)
seth.backward(l)
seth.right(90)
seth.forward(l/2)
seth.penup()
seth.forward(l/2)
seth.left(90)
seth.forward(l/4)
seth.right(180)
#–¥S
seth.pendown()
seth.circle(l/4,270)
seth.circle(-l/4,270)
seth.penup()
seth.forward(3*l/4)
seth.left(90)
seth.forward(l/2)
#–¥X
seth.pendown()
seth.left(60)
seth.forward(2*l/math.sqrt(3))
seth.penup()
seth.left(120)
seth.fd(l/math.sqrt(3))
seth.left(120)
seth.pendown()
seth.forward(2*l/math.sqrt(3))


window.exitonclick()
