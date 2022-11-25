import turtle
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # Used for calling when object instance
        self.segments = []
        self.create_snake()
        self.head_snake = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())#-1 count from last in list

    def move(self):
        """Hard coded: 2 is decrease to 1 and 1 to 0 by sub(-1)
        and while decreasing from number 2 to 1 [new_x = segments[seg_num - 1].xcor(),new_y = segments[seg_num - 1].ycor()
        getting location of index 1 by xcord and ycord eg:(xcord = -20,ycord = 0)and moving by
        segments[seg_num] where seg_num has 2 for this example now index 2 will move to ,[goto(new_x, new_y)] to index 1 and continues ]  """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.head_snake.forward(MOVE_DISTANCE)

    def up(self):
        # if head of snake is not in down then move upward
        # self.head_snake.heading() this gives Direction of heading, and it will check with const Value which is DOWN
        if self.head_snake.heading() != DOWN:
            self.head_snake.setheading(UP)

    def down(self):
        if self.head_snake.heading() != UP:
            self.head_snake.setheading(DOWN)

    def left(self):
        if self.head_snake.heading() != RIGHT:
            self.head_snake.setheading(LEFT)

    def right(self):
        if self.head_snake.heading() != LEFT:
            self.head_snake.setheading(RIGHT)
