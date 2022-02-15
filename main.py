from turtle import Turtle, Screen
from random import randint, shuffle
from tkinter.messagebox import showinfo

from better import bet_turtle

user_bet = bet_turtle()
print(f"You chose {user_bet} turtle.")

is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)
showinfo(title='CHOOSING', message=f"You chose {user_bet} turtle.")


def create_hipodrom():
    worker = Turtle()
    worker.speed("fastest")
    worker.hideturtle()
    for i in range(6):
        worker.penup()
        worker.goto(x=-250, y=-100 + 30 * i)
        worker.pendown()
        worker.forward(500)
    worker.penup()
    worker.goto(x=-250, y=-100)
    worker.pendown()
    worker.goto(x=-250, y=-100 + 6 * 30)
    worker.forward(500)
    worker.goto(x=250, y=-100)

create_hipodrom()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-85, -55, -25, 5, 35, 65]
all_turtles = []

#Create 6 turtles
for indx in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[indx])
    if colors[indx] == user_bet:
        new_turtle.goto(x=-240, y=y_positions[indx] - 10)
        new_turtle.write("BET", move=False, align="left", font=("Arial", 12, "bold"))
    new_turtle.goto(x=-240, y=y_positions[indx])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    shuffle(all_turtles)
    for turtle in all_turtles:
        #Make each turtle move a random amount.
        turtle.forward(randint(1, 10))
        # print(turtle.pencolor())

        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 234:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
                showinfo(title='WON', message=f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
                showinfo(title='LOST', message=f"You've lost! The {winner} turtle is the winner!")
            break

screen.exitonclick()