from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0,y=270)
        self.write(f"Score:{self.points}", move=False, align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGMENT,font=FONT)


    def update_score(self):
        self.points += 1
        self.clear()
        self.write(f"Score:{self.points}", move=False, align=ALIGMENT, font=FONT)

