from turtle import*

LIST_CONST = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        
        self.ready = []
        self.make_snake()
        self.head = self.ready[0]

    
    def make_snake(self):
         
        for squre in LIST_CONST :
            self.add_snake(squre)

    
    def add_snake(self, position):
        
        new_snake = Turtle(shape = "square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.ready.append(new_snake)

    
    def extend(self):
        self.add_snake(self.ready[-1].position())


    def move(self):
        
        for segment in range(len(self.ready) -1 , 0, -1):
            new_x = self.ready[segment - 1].xcor()
            new_y = self.ready[segment - 1].ycor()
            self.ready[segment].goto(new_x, new_y)

        self.head.color("orange")
        self.head.forward(MOVE_DISTANCE)
        
    
    def move_up(self):
        
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def move_down(self):
       
       if self.head.heading() != UP:
        self.head.setheading(DOWN)

    
    def move_left(self):
        
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    
    def move_right(self):
        
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        
        
        
       