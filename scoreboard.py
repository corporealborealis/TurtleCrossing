from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level_no = 1
        self.penup()
        self.goto(-280,250)
        self.write(f'Level:{self.level_no}', align='left', font=FONT)


    def update_score(self):
        self.clear()
        self.level_no += 1
        self.write(f'Level:{self.level_no}', align='left', font=FONT)







