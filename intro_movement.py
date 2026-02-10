import time, turtle, random
from utils import *
# Section 1: Setup
set_background("clouds.gif")
s1 = create_sprite("cookie.gif",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 5
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 5
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 5
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 5
    y = s1.ycor() 
    s1.goto(x,y)

def draw():
    s1.pendown()
def stop_drawing():
    s1.penup()
def green_pen():
    s1.color("green")
def blue_pen():
    s1.color("blue")
def red_pen ():
    s1.color("red")
def yellow_pen():
    s1.color("yellow")

window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(draw, "c")
window.onkeypress(stop_drawing, "space")
window.onkeypress(green_pen, "g")
window.onkeypress(blue_pen, "b")
window.onkeypress(red_pen, "r")
window.onkeypress(yellow_pen, "y")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()