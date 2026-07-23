from turtle import Turtle
import random

class FoodSnake(Turtle):
    def __init__(self):
        '''Initializes a food object born from the Turtle class and sets its attributes and methods.'''
        super().__init__()
        self.shape("circle")
        self.color("green1")
        self.speed(0)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        '''Spawns the food at a new random location within the game boundaries.'''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
