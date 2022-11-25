from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")

screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
scoreboard = Score()
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head_snake.distance(food) < 15:
        scoreboard.count_score()
        food.refresh()
        snake.extend()

    # Detect collision with tail
    if snake.head_snake.xcor() > 280 or snake.head_snake.xcor() < -280 or snake.head_snake.ycor() > 280 or snake.head_snake.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

        # Detect collision with tail
        # snake.segments[1:]: gives all segments except head.
        for segment in snake.segments[1:]:
            # distance between snake head and snake segments
            if snake.head_snake.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
# one way of detecting collision.
# Detect collision with tail
# if collision occurs from any segment which is currently running then game is finished.
#     for segment in snake.segments:
#         # if current head then, don't check distance or don't detect collision.
#         if segment == snake.head_snake:
#             pass
#         # distance between snake head and snake segments
#         elif snake.head_snake.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()
