from turtle import Turtle
from random import randint


class Racer(Turtle):
    def __init__(self, color):
        super().__init__()
        self.color(color)
        self.shape("turtle")
        self.bet = False
        self.penup()

    def random_run(self):
        self.forward(randint(2, 6))

    def go_starting_box(self, x, y):
        self.penup()
        if self.bet == True:
            self.goto(x=x, y=y-10)
            self.write("BET", move=False, align="left", font=("Arial", 12, "bold"))
        self.goto(x=x, y=y)

    def bet_on(self):
        self.bet = True

    @classmethod
    def bet_turtle(cls, racers: list, color: str):
        cls.clear_bets(racers)
        for racer in racers:
            if color == racer.pencolor():
                racer.bet = True

    @classmethod
    def clear_bets(cls, racers: list):
        for racer in racers:
            racer.bet = False
