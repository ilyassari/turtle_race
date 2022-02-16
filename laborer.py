from turtle import Turtle

class Laborer(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()

    def draw_hipodrom(self):
        for i in range(6):
            self.penup()
            self.goto(x=-250, y=-100 + 30 * i)
            self.pendown()
            self.forward(500)
        self.penup()
        self.goto(x=-250, y=-100)
        self.pendown()
        self.goto(x=-250, y=-100 + 6 * 30)
        self.forward(500)
        self.goto(x=250, y=-100)

    def write_title(self):
        self.penup()
        self.goto(x=-120, y=100)
        self.write("TURTLE RACE", move=False, align="left", font=("Segoe UI Semibold", 24, "bold italic"))

