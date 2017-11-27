import turtle

def draw_triangle(seth,l):
    seth.fillcolor("green")
    seth.fill(True)
    seth.forward(l)
    seth.right(120)
    seth.fd(l)
    seth.right(120)
    seth.fd(l)
    seth.right(120)
    seth.fill(False)
    
window = turtle.Screen()
window.bgcolor("white")
jack = turtle.Turtle()
jack.shape("turtle")
jack.color("green")
jack.pencolor("blue")
jack.shapesize(1,1,1)
l = 25
jack.seth(60)
i= 0
j = 0
n = 0
while n < 3:
    j = 0
    while j < 3:
        i = 0
        while i < 4:
            i = i+1
            draw_triangle(jack,l)
            jack.fd(l)
        j = j+1
        jack.right(120)
    jack.fd(8*l)
    jack.right(120)
    n = n+1

window.exitonclick()
