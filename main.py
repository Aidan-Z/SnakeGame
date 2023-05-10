from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time



def main():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('SNAKE')
    screen.tracer(0)  # tracer

    snake = Snake()  # snake object
    food = Food()
    s = ScoreBoard()

    screen.listen()
    # screen.onkey(s.game_over, "space")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    s.game_score()
    game_on = True
    while game_on:
        screen.update() #update screen after each segment is already in place- outside 'for loop' so pieces move together
        time.sleep(0.1)  # adding delay after each movement- refresh screen every 0.1 seconds

        snake.move()

        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_snake()
            s.add_score()

        #detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            s.reset()
            snake.reset()
            # game_on = False
            # s.game_over()

        #detect collision with tail
        for i in snake.segments[1:]:
            if snake.head.distance(i) <10:
                s.reset()
                snake.reset()
                # game_on = False
                # s.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()



