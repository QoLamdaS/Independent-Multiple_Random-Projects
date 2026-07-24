from turtle import Turtle, Screen
import random

#* Calculate dynamic wall boundaries based on actual screen size
half_width = Screen().window_width() / 2 - 20 #TODO: The food doensn't spawn outside of the previous wall. NEED TO BE REALLY MORE RANDOM FOOD SPAWNING BUG
half_height = Screen().window_height() / 2 - 20 #TODO: The food doensn't spawn outside of the previous wall. NEED TO BE REALLY MORE RANDOM FOOD SPAWNING BUG

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
        random_x = random.randint(-int(half_width), int(half_width)) #TODO: The food doensn't spawn outside of the previous wall. NEED TO BE REALLY MORE RANDOM FOOD SPAWNING BUG
        random_y = random.randint(-int(half_height), int(half_height)) #TODO: The food doensn't spawn outside of the previous wall. NEED TO BE REALLY MORE RANDOM FOOD SPAWNING BUG
        self.goto(random_x, random_y)
