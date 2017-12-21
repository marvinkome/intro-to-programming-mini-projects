import turtle

def draw_square_fw(some_turtle, color='yellow'):
    
    some_turtle.shape('arrow')
    some_turtle.color(color)
    some_turtle.speed(50)

    for movement in range(4): 
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle_fw(some_turtle, color='yellow'):
    
    some_turtle.color(color)
    some_turtle.shape('arrow')
    some_turtle.speed(50)
    some_turtle.circle(50)

def draw_triangle_fw(some_turtle, color='yellow'):
    
    some_turtle.color(color)
    some_turtle.speed(50)
    some_turtle.forward(100)
    some_turtle.left(120)
    some_turtle.forward(100)
    some_turtle.left(120)
    some_turtle.forward(100)

def draw_art():
    brad = turtle.Turtle()

    for i in range(36):
        draw_triangle_fw(brad,'white')
        draw_circle_fw(brad,'yellow')
        draw_square_fw(brad,'green')
        brad.right(10)

WINDOW = turtle.Screen()
WINDOW.bgcolor('black')

draw_art()
#draw_circle()

WINDOW.exitonclick()
