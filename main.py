from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

number_of_segments = 3
x_position = 0

for _ in range(number_of_segments):
    snake = Turtle("square")
    snake.color("white")
    snake.setpos(x=x_position,y=0)
    x_position -= 20





























screen.exitonclick()