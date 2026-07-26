from turtle import Turtle, Screen
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
        self.screen = Screen() #? Save reference to the active window so refresh() can check its true pixel dimensions
        self.refresh()

    def refresh(self):
        '''Spawns the food at anywhere across the current screen width/height'''
        random_x = random.randint(-int(self.screen.window_width() // 2 - 20), int(self.screen.window_width() // 2 - 20))
        random_y = random.randint(-int(self.screen.window_height() // 2 - 20), int(self.screen.window_height() // 2 - 20))
        self.goto(random_x, random_y)
