from turtle import*
from food import*
import random
import time
from food import Food
from make_snake import*
from scorebord import*


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game by Tokkyman")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up" ,fun = snake.move_up)
screen.onkey(key="Down" ,fun = snake.move_down)
screen.onkey(key="Left" ,fun = snake.move_left)
screen.onkey(key="Right" ,fun = snake.move_right)


game_on = True

while game_on:
        
    screen.update()
    time.sleep(0.1)
    snake.move() 

# to recreate the food every time snake got it and add the score by 1
    if snake.head.distance(food) <= 15:
        food.re_state_food()
        snake.extend()
        score.add_score()

#to detect if snake is on the wall?
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or  snake.head.ycor() <= -300 :
        score.game_over()
        game_on = False  
        
#to check if snake eat them self
    for square in snake.ready[1:]:
        
        if snake.head.distance(square) < 10:
            score.game_over()
            game_on = False  


screen.exitonclick()