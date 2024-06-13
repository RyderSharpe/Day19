# TODO - Pop up asks you to bet who will win race (enter a colour).
# TODO - Turts line up in starting positions.
# TODO - Turts start racing
# TODO - First to cross finish line prints out what colour won

from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("DeepSkyBlue")
screen.setup(750, 450)
# Set the background image
try:
    screen.bgpic('C:/Users/rsharpe/PycharmProjects/day19/r.gif')
except Exception as e:
    print(f"Error loading background image: {e}")

start_line = -360
finish_line = 320

screen.title("Welcome to the turtle race!")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "white"]
turts = ["turt_red", "turt_orange", "turt_yellow", "turt_green", "turt_blue", "turt_purple", "turt_cyan", "turt_white"]
all_turtles = []

def players_line_up():
    x_axis = start_line
    y_axis = -160
    for turt_name in turts:
        new_turtle = Turtle(shape="turtle")
        new_turtle.shapesize(stretch_wid=2, stretch_len=2, outline=1)
        new_turtle.color(colors[turts.index(turt_name)])
        new_turtle.penup()
        new_turtle.speed(9)
        new_turtle.goto(x=x_axis, y=y_axis)
        y_axis += 43
        print(turt_name)
        all_turtles.append(new_turtle)

def validate_user_color(prompt="Which Turt will win the race? Enter a colour"):
  """
  This function keeps prompting the user for a color until a valid choice
  from the `colors` list is entered. It returns the validated color or None
  if the user cancels the input dialog.
  """
  while True:
    user_bet = screen.textinput("Make your bet", prompt)
    if user_bet is None:  # Handle canceled input
      return None
    elif user_bet.lower() in colors:  # Check for case-insensitive match
      return user_bet.lower()  # Ensure consistency by returning lowercase
    else:
      print("Invalid color. Please choose from:", colors)

players_line_up()
user_bet = validate_user_color()

is_race_on = False  # Initialize is_race_on to False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= finish_line:  # Use >= for finish line comparison
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} won! You won the bet!")
            else:
                print(f"{winning_color} won. You lost the bet.")
            is_race_on = False  # Set is_race_on to False to stop the loop
            break  # Exit the for loop once the race is over

# Keep the window open until closed manually
screen.exitonclick()

