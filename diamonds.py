import turtle

def draw_diamond(seth,l):
    seth.forward(l)
    seth.right(60)
    seth.fd(l)
    seth.right(120)
    seth.fd(l)
    seth.right(60)
    seth.fd(l)
    seth.right(120)

i = 0
window = turtle.Screen()
window.bgcolor = ("white")
l = 100
jack = turtle.Turtle()
jack.pencolor("blue")
jack.seth(30)
jack.speed(100)
jack.shape("turtle")
jack.color("blue")
while i<=360 :
    draw_diamond(jack,l)
    jack.right(5)
    i = i + 5

jack.seth(270)
jack.fd(4*l)

window.exitonclick()
