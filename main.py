import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_board

screen = Screen()

screen.setup(600,600)
screen.bgcolor("black") # here  bg color is a attribute that defines the color of the background of the screen.
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score_board()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")





game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food.
    if snake.segments[0].distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
     #detect collision with wall

    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        game_is_on = False
        scoreboard.gameover()
    #Detect collision with tail .

    for segment in snake.segments[1:]:

        if snake.segments[0].distance(segment)<10:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()