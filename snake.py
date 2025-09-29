from turtle import Turtle

class Snake():

    def __init__(self):
        self.number_of_segments = 3
        self.x_position = 0
        self.segments = []

        for _ in range(self.number_of_segments):
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.setpos(x=self.x_position, y=0)
            self.x_position -= 20
            self.segments.append(snake_segment)

    def move (self):

        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

