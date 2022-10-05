from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from turtle import*
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("green")
        self.speed("fastest")
        self.re_state_food()
        

    def re_state_food(self):
        random_x = random.randint(-260 , 260)
        random_y = random.randint(-260 , 260)
        self.goto(random_x, random_y)
