from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class SnakeBody:
    def __init__(self):
        '''Initializes the snake body object born and sets its attribute and method.'''
        self.segments = []
        self.create_snake()

    def create_snake(self):
        ''''Create the initial/default snake body with three segments right after the game starts.'''
        for position in starting_positions:
            self.add_segment(position) 

    def add_segment(self, position):
        '''Add a new segment to the snake at the given position.'''
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        '''Add a new segment to the snake at the position of the last segment.'''
        self.add_segment(self.segments[-1].position()) #! .position() method; returns its current (x, y) coordinates of the last segment (the tail).

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

