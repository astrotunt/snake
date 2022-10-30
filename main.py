from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek")



snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

screen.tracer(0)
not_game_over = True

while not_game_over:
    snake.move()
    screen.update()
    time.sleep(snake.speed)
    scoreboard.display_score()
    if snake.segments[0].distance(food) < 15:
        food.goto(random.randint(-280,280),random.randint(-280,280))
        snake.extend()
        snake.speed -= 0.005
        scoreboard.increase_score()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        scoreboard.lives -= 1
        scoreboard.reset()
        time.sleep(2)
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.lives -= 1
            scoreboard.reset()
            time.sleep(2)
            snake.reset()
    if scoreboard.lives == 0:
        not_game_over = False
with open("data.txt", mode="w") as file:
    file.write(str(scoreboard.high_score))
screen.exitonclick()