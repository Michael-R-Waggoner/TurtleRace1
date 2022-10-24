from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Choose a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.setx(-240)
    new_turtle.sety(turtle_index * 30 - 90)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! {winning_color} won!")
            else:
                print(f"You Lost! {winning_color} won!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()