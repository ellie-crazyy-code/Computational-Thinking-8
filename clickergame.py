import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("underwater.gif")
create_sprite("eggs.webp")
create_sprite("bakingsoda.png")
create_sprite("milkjug.gif")
create_sprite("cake.png")

print ("press the 'b' key to add baking soda")
print ("press the 'e' key to add eggs")
print ("press the 'm' key to add milk")
print ("once you have enough ingredients, press the 'space' key to make a cake!")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
eggs = 0
bakingsoda = 0
milkjug = 0
cake = 0



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def add_eggs():
    global eggs
    eggs =+1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("eggs.webp x,y")

def add_bakingsoda():
    global bakingsoda
    bakingsoda =+1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite ("bakingsoda.png x,y")


def add_milkjug():
    global milkjug
    milkjug =+1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite ("milkjug.gif x,y")

def make_cake ():
     if add_bakingsoda >= 10 and add_eggs >= 7 and add_milkjug >= 3:
        cake_control =+1
def add_cake():
    global cake
    cake =+1
    x = (-200,200)
    y = (-200,200)
    create_sprite ("cake.png x,y")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    # message_sprite.clear()
    # message_sprite.write(f"bakingsoda:{bakingsoda_control}/n eggs:{eggs_control}/n milk:{milkjug_control}/n cakes:{cake_control}")
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()