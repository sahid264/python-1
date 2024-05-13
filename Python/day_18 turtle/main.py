# from turtle import Turtle,Screen
# import random

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")

# # draw a square

# # for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# draw a dashed line

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()




# draw different shapes with different colours
# colours = ["red","blue","yellow","green","pink","brown","black","violet"]

# def draw_shapes(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)


# for shapes in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shapes(shapes)


# draw a random walk
# colours = ["red","blue","yellow","green","pink","brown","black","violet"]
# direction = [0,90,180,270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")

# for _ in range(100):
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(direction))

# draw a spirograph
#   RGB
# import turtle as t
# import random

# tim = t.Turtle()

# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)

#     return color


# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)
