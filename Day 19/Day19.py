import turtle

#create turtle
tim = turtle.Turtle()
screen = turtle.Screen()

#functions
def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def to_right():
    tim.right(30)

def to_left():
    tim.left(30)

def clear():
    screen.reset()

#play
screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(to_right, 'd')
screen.onkey(to_left, 'a')
screen.onkey(clear, 'c')

#exit
screen.exitonclick()