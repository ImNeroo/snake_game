from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.show_score()

    def sum_score(self):
        self.current_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over.", move=False, align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)
