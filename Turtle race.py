# TODO - pop up asks you to bet who will win race (enter a colour).
# TODO - Turts line up in starting positions.
# TODO - Turts start racing
# TODO - first to cross finish line prints out what colour won

#user_bet = screen.textinput("Make your bet", "Which turt will win the race? Enter a colour")

from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("DeepSkyBlue")
screen.setup(500, 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turts = ["turt_red", "turt_orange", "turt_tellow", "turt_green", "turt_blue", "turt_purple"]

x_axis = -230
y_axis = -120

for turt_name in turts:
    player = Turtle(shape="turtle")
    player.color(colors[turts.index(turt_name)])
    player.penup()
    player.goto(x=x_axis, y=y_axis)
    y_axis += 50


# Keep the window open until closed manually
screen.exitonclick()


