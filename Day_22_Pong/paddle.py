from turtle import Turtle
MOVE_DISTANCE = 10
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.x, self.y = coordinates
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x, self.y)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
