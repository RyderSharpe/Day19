from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

# Get ahold of the screen object

def move_forward():
    t.forward(10)

def move_backwards():
    t.forward(-10)

def counter_clockwise():
    t.tilt(5)

def clockwise():
    t.tilt(-5)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.exitonclick()