from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score}",align = "center", font =("arial",24,"normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.high_score}", align="center", font=("arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../snake_game/data.txt", "w") as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.update_scoreboard()



    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
