import turtle as turtle_module
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst.jpg",30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(245, 240, 231), (226, 234, 242), (245, 232, 238), (231, 243, 237), (203, 159, 104), (231, 212, 105), (47, 103, 139), (133, 168, 191), (145, 81, 61), (198, 140, 162), (144, 67, 85), (25, 39, 53), (140, 178, 153), (198, 92, 73), (166, 156, 59), (62, 116, 93), (188, 92, 120), (26, 44, 36), (222, 172, 187), (60, 44, 33), (49, 158, 179), (91, 154, 109), (224, 176, 169), (43, 59, 99), (180, 189, 212), (15, 94, 73), (237, 211, 7), (101, 125, 165), (63, 35, 45), (172, 204, 183)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101
for dot_count in range(1 , number_of_dots):
    tim.dot(25,random.choice(color_list) )
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
