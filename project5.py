import turtle, time, random
from utils import *

set_background("spring.gif")
s1 = create_sprite("mlp.gif", 0,-200)
s2 = create_sprite("cookie.gif")

cookie = 0
score = 0

sprite_list = [s2]

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

window.listen()
for i in range(1000000000):

    # def add_cookie():
    #     global cookie
    if i % 300 == 0:
        x = random.randint (-300, 300)
        y = random.randint (-300, 300)
        item = create_sprite ("cookie.gif", x,y)
        item.setheading (270)
        sprite_list.append (item)
    for s2 in sprite_list:
        if get_distance(s2, s1) <100:
            sprite_list.remove(s2)
            cookie +=1
            #s2.goto(-15000,-15000)
            #s2.hideturtle()

    if cookie >= 10:
        print ("YOU WIN!!")

    time.sleep(0.01)
    window.update()