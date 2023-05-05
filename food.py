from turtle import Turtle
import random
#food generates as a red 10x10 circle which will apear at a random location on screen when the food obj is generated
class Food(Turtle):

    def __init__(self):
        super().__init__() #super() class constructor
        #inheriting these methods from Turtle class and module... would have to create them from scratch otherwise
        self.shape("circle") #when food object created, it is already circle
        self.penup() #will be pen up
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #and will have a size of 10x10
        self.color('red')
        self.speed(0)
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # go to random x,y location on screen
