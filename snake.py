from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for turtle_index in STARTING_POSITIONS:
            self.add_segment(turtle_index)

    def add_segment(self, turtle_index):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(turtle_index)
        self.segment.append(new_square)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for square in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[square - 1].xcor()
            new_y = self.segment[square - 1].ycor()
            self.segment[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
