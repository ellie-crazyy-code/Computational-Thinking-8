import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =+-350
y1 =+-200
x2 =+-350
y2 =+-100
x3 =+-350
y3 =+ 100
x4 =+-350
y4 =+ 200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("clouds.gif")
t1 = create_sprite("fish.gif",x1,y1)
t2 = create_sprite("fox.gif",x2,y2)
t3 = create_sprite("soccerball.gif",x3,y3)
t4 = create_sprite("basketball.gif",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - sprite 3 is the fastest so it will always win!
for i in range(30):
    x1 += 30
    x2 += 25
    x3 += 45
    x4 += 40

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# Section 4 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print ("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print ("player 2 wins!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    print ("player 3 wins!")
elif x4 >= x2 and x4 >= x3 and x4 >= x1:
    print ("player 4 wins!")


turtle.exitonclick()