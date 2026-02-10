import turtle, time, random
from utils import *

set_background("spring.gif")
s1 = create_sprite("mlp.gif", 0,-200)
s2 = create_sprite("cookie.gif")

cookies = 0
score = 0

print ("instructions: move rainbow-dash (with the 'wasd' keys) to eat cookies!")
print ("when you get 10 cookies you WIN!!")

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

window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

def add_cookies():
    global cookies
    cookies =+1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("cookies.gif x,y")

if cookies >= 10:
    print ("YOU WIN!!")

    window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()