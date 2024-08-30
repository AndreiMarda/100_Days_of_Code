import turtle as t
from random import choice

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.shape("turtle")
tim.hideturtle()

color_list = [(219, 148, 87), (52, 106, 137), (152, 84, 54), (218, 230, 238), (232, 242, 237), (121, 162, 187), (144, 66, 93), (218, 86, 60), (204, 128, 154), (166, 151, 45), (43, 38, 31), (51, 123, 85), (198, 86, 118), (27, 48, 70), (117, 180, 152), (74, 160, 121), (230, 201, 113), (40, 56, 108), (50, 35, 47), (28, 48, 38), (120, 35, 56), (241, 159, 183), (102, 120, 169), (47, 159, 179), (247, 167, 154), (8, 102, 76), (112, 43, 34), (154, 212, 187)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.dot(20, choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()