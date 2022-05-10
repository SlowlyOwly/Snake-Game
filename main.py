from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

snake.body()

screen.listen()
screen.onkey(snake.turn_up, "w")
screen.onkey(snake.turn_down, "s")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 1:
        food.refresh()
        if food.position() == snake.segments:
            food.refresh()
        snake.add_segment()
        score.clear()
        score.new_score()

    # Collision with walls
    if snake.head.xcor() == -300:
        game_on = False
        score.game_over()
    elif snake.head.xcor() == 300:
        game_on = False
        score.game_over()
    elif snake.head.ycor() == -300:
        game_on = False
        score.game_over()
    elif snake.head.ycor() == 300:
        game_on = False
        score.game_over()

    # Collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
