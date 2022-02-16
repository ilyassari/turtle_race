from turtle import Turtle, Screen
from random import randint, shuffle
from tkinter.messagebox import showinfo, askyesno

from racer import Racer
from laborer import Laborer
from color_picker import choose_color

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [65, 35, 5, -25, -55, -85]

def game():

    bet_color = choose_color()

    all_racers = list()
    for color in COLORS:
        new_one = Racer(color)
        all_racers.append(new_one)

    Racer.bet_turtle(all_racers, bet_color)

    screen = Screen()
    screen.setup(width=600, height=400)

    # Draw hipodrom
    laborer = Laborer()
    laborer.write_title()
    laborer.draw_hipodrom()

    #Turtles to Starting box
    for turtle, y in zip(all_racers[::-1], Y_POSITIONS[::-1]):
        turtle.go_starting_box(x=-240, y=y)

    showinfo(title='CHOOSING', message=f"You bet on {bet_color} turtle.")

    race_on = True

    while race_on:
        shuffle(all_racers)

        for turtle in all_racers:
            #Make each turtle move a random amount.
            turtle.random_run()

            #230 is 250 - half the width of the turtle.
            if turtle.xcor() > 234:
                race_on = False
                winner = turtle.pencolor()
                if winner == bet_color:
                    print(f"You've won! The {winner} turtle is the winner!")
                    showinfo(title='WON', message=f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner} turtle is the winner!")
                    showinfo(title='LOST', message=f"You've lost! The {winner} turtle is the winner!")
                Racer.clear_bets(all_racers)
                screen.exitonclick()
                break

game()


