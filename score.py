from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.the_score = 0
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.hideturtle()
        self.speed(0)


    def game_score(self):
        self.write(f"Score: {self.the_score}", align='center', font=('Helvetica', 20, 'normal'))


    def add_score(self):
        self.clear()
        self.the_score += 1
        self.game_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Helvetica', 20, 'bold'))








