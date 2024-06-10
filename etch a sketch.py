from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.bgcolor("dodger blue")
t.pensize(2)
# Get ahold of the screen object

def move_forward():
    t.forward(10)

def move_backwards():
    t.forward(-10)

def left_turn():
    t.left(5)
    # CLASS
    # new_heading = t.heading() + 10
    # t.setheading(new_heading)

def right_turn():
    t.right(5)

def clear():
    t.penup()
    t.clear()
    t.home()
    t.pendown()

# Listen for key-presses on the screen
screen.listen()

# Bind movement functions to keys
screen.onkey(key='Up', fun=move_forward)
screen.onkey(key='Down', fun=move_backwards)
screen.onkey(key='Left', fun=left_turn)
screen.onkey(key='Right', fun=right_turn)
screen.onkey(key="c", fun=clear)


# Keep the window open until closed manually
screen.exitonclick()