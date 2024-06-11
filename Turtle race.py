# TODO - pop up asks you to bet who will win race (enter a colour).
# TODO - Turts line up in starting positions.
# TODO - Turts start racing
# TODO - first to cross finish line prints out what colour won

from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("DeepSkyBlue")
screen.setup(750, 450)
# Set the background image
try:
    screen.bgpic('C:/Users/rsharpe/PycharmProjects/day18/b.gif')
except Exception as e:
    print(f"Error loading background image: {e}")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "black"]
turts = ["turt_red", "turt_orange", "turt_yellow", "turt_green", "turt_blue", "turt_purple", "turt_cyan", "turt_black"]

def players_line_up():
    x_axis = -340
    y_axis = -160
    for turt_name in turts:
        player = Turtle(shape="turtle")
        player.shapesize(stretch_wid=2, stretch_len=2, outline=1)
        player.color(colors[turts.index(turt_name)])
        player.penup()
        player.goto(x=x_axis, y=y_axis)
        y_axis += 43
        print(turt_name)

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


# is_race_on = False
# user_bet = validate_user_color()
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     random.randint(0,10)


players_line_up()
validate_user_color()


# Keep the window open until closed manually
screen.exitonclick()


