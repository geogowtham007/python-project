import turtle as t

screen = t.Screen()
screen.title("Drawing GOWTHAM")
screen.bgcolor("black")

pen = t.Turtle()
pen.shape("turtle")
pen.speed(1)
pen.pensize(5)
pen.color("yellow")

def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
move(-250,50)

pen.setheading(0)
pen.forward(40)
pen.backward(40)
pen.right(90)
pen.forward(60)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(25)
pen.left(90)
pen.forward(20)


move(-180, 50)
pen.setheading(0)
for i in range(2):
    pen.forward(40)
    pen.right(90)
    pen.forward(60)
    pen.right(90)


move(-110, 50)
pen.setheading(270)
pen.forward(60)
pen.left(150)
pen.forward(35)
pen.right(120)
pen.forward(35)
pen.left(150)
pen.forward(60)


move(-50, 50)
pen.setheading(0)
pen.forward(50)
pen.backward(25)
pen.right(90)
pen.forward(60)


move(25, 50)
pen.setheading(270)
pen.forward(60)
pen.backward(30)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(30)
pen.backward(60)


move(90, -10)
pen.setheading(75)
pen.forward(65)
pen.right(150)
pen.forward(65)
pen.backward(30)
pen.right(105)
pen.forward(19)


move(150, -10)
pen.setheading(90)
pen.forward(60)
pen.right(150)
pen.forward(35)
pen.left(120)
pen.forward(35)
pen.right(150)
pen.forward(60)

move(220,-50)
pen.color("red")
pen.pensize(10)
pen.setheading(100)
pen.left(80)
pen.forward(505)
pen.right(90)
pen.forward(140)
pen.right(90)
pen.forward(505)
pen.right(90)
pen.forward(140)

pen.hideturtle()

t.done()
