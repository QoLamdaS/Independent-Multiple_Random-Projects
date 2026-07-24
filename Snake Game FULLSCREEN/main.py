from turtle import Screen
from the_snake_body import SnakeBody
from the_food import FoodSnake
from the_scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Extended🐍Snake_Game🖥️FULLSCREEN!!!!")
screen.tracer(0)

#* Enable Native Fullscreen
canvas_root = screen.getcanvas().winfo_toplevel()
canvas_root.attributes("-fullscreen", True)

screen.onkey(screen.bye, "Escape") # Optional: Press 'Escape' to exit fullscreen easily

#* Calculate dynamic dynamic wall boundaries based on actual screen size
half_width = screen.window_width() / 2 - 20
half_height = screen.window_height() / 2 - 20

snake = SnakeBody()
food = FoodSnake() 
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15: 
        #* Detect collision with food; a.k.a detect Snake eating the random spawned food and then grow 'get longer'.
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor() > half_width or snake.segments[0].xcor() < -half_width or snake.segments[0].ycor() > half_height or snake.segments[0].ycor() < -half_height:
        #* Detect collision with wall; a.k.a detect Snake hitting the maximum wall from player view
        break

    for segment in snake.segments[1:]: #! The very first segment is the Snake's head, so starting from the second segment is the best idea to skip the Snake's head.
        #* Detect collision with itself; a.k.a detect Snake hitting its own body
        if snake.segments[0].distance(segment) < 10:
            break

score.game_over()
screen.mainloop()

