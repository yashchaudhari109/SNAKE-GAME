from turtle import Screen,Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard




screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect coloision with tail.
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()


# Todo take user name and keep user score record.
# Todo show highest score and current score at the end of the game.
# Todo show user why he lose does he hit the wall or collide with his own body.
# Todo ask user to choose the snake color.
# Todo change the shape of the food to the actual fruit.
# Todo add extra set of keys to operate snake.
# Todo ask user to choose a level (set snake move time accordingly)
