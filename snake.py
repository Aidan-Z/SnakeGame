from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

#each time we create 'snake' object, it creates a 3-segment snake:
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake() #class method
        self.head = self.segments[0]


    def create_snake(self):
        for i in STARTING_POSITIONS: #for each element (tuple with starting position) in list: (so 3)
            self.add_body(i)


    def add_body(self, i): #extend snake
        new_segment = Turtle('square')  # create a new instance of Turtle() class
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(i)  # go to the position we are itterating over in list (1st, 2nd, 3rd)
        self.segments.append(new_segment)  # add the 'self.' to show that we refer to class attribute

    def reset(self):
        for i in self.segments:
            i.goto(1000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_snake(self):
        self.add_body(self.segments[-1].position()) #get the last position of segment in list by using method .position()

    def move(self):

        #make the LAST segment (instance) go to the position of the SECOND LAST segment, which goes to position of FIRST seg
        for i in range(len(self.segments)-1, 0, -1): #reverse range (negetive step, goes from highest to lowest)
            new_x = self.segments[i-1].xcor() #getting the x coordinate of second last (i-1 will always be the movement prior)
            new_y = self.segments[i-1].ycor() #getting the previous y cord
            self.segments[i].goto(new_x, new_y) #telling the current instance to go to the previous cord location

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
         self.head.setheading(0)



