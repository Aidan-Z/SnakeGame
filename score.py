from turtle import Turtle

with open('highscore.txt', mode='r') as f:
    highest_score = f.read()

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.the_score = 0
        self.high_score = int(highest_score)
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.hideturtle()
        self.speed(0)




    def game_score(self):
        self.clear()
        self.write(f"Score: {self.the_score}  High Score: {self.high_score}", align='center', font=('Helvetica', 20, 'normal'))

    def reset(self):
        if self.the_score > self.high_score:
            self.high_score = self.the_score
            with open('highscore.txt', mode='w') as f:
                f.write(str(self.high_score))
        self.the_score = 0
        self.game_score()

    def add_score(self):
        self.the_score += 1
        self.game_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align='center', font=('Helvetica', 20, 'bold'))
    #     #works but need way to end whileloop








