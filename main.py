from turtle import  Screen
from snakee import Snake
import time
from score import Scoreboard
from food import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake arena")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 1:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()