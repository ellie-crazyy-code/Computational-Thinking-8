will_points = 0
mike_points = 0
lucas_points = 0
eleven_points = 0
max_points = 0
dustin_points = 0

print ("which stranger things character are you most like? take this quiz to find out!!")

answer1 = input ("which do you value the most? a: loyalty b: trust c: empathy d: friendship e: determination f: leadership?")
if answer1 == "a":
    lucas_points += 1
elif answer1 == "b":
    eleven_points =+ 1
elif answer1 == "c":
    will_points += 1
elif answer1 == "d":
    dustin_points += 1
elif answer1 == "e":
    max_points += 1
elif answer1 == "f":
    mike_points += 1

answer2 = input ("what color do you prefer wearing? a: yellow b: navy blue C: green d: purple e: light blue f: red")
if answer2 == "a":
        mike_points += 1
elif answer2 == "b":
        will_points += 1
elif answer2 == "c":
        dustin_points +=1
elif answer2 == "d":
        eleven_points +=1
elif answer2 == "e":
        max_points += 1
elif answer2 == "f":
        lucas_points +=1
    
answer3 = input ("which food do you prefer? a: waffles b: chocolate c: Scoops Ahoy ice cream d: reece's pieces e: pasta bolognese f: pizza")
if answer3 == "a":
    eleven_points +=1
elif answer3 == "b":
    dustin_points +=1
elif answer3 == "c":
    max_points +=1
elif answer3 == "d":
    will_points +=1
elif answer3 == "e":
    mike_points +=1
elif answer3 == "f":
    lucas_points +=1

answer4 = input ("what activity would you prefer to do on a saturday afternoon with friends? a: play a board game b: go to the mall c: watch a movie d: go on a bike ride e: make out with your girlfriend/boyfriend?")
if answer4 == "a":
    will_points +=1
elif answer4 == "b":
    max_points +=1 
    eleven_points +=1
elif answer4 == "c":
    dustin_points +=1
elif answer4 == "d":
    lucas_points +=1
elif answer4 == "e":
    mike_points +=1

answer5 = input ("pick a song: a: sk8ter boy b: juliet c: christmas kids d: die with a smile e: tree house f: don't stop believing")
if answer5 == "a":
    max_points +=1
elif answer5 == "b":
    will_points +=1
elif answer5 == "c":
    eleven_points =+1
elif answer5 == "d":
    lucas_points +=1
elif answer5 == "e":
    dustin_points +=1
elif answer5 == "f":
    mike_points +=1
     
if max_points > will_points and max_points> mike_points and max_points > lucas_points and max_points > dustin_points and max_points > eleven_points:
    print (f"you are most like max mayfield")
elif will_points > mike_points and will_points > lucas_points and will_points > dustin_points and will_points > eleven_points:
    print (f"you are most like will byers")
elif mike_points > lucas_points and mike_points > dustin_points and mike_points > eleven_points:
    print (f"you are most like mike wheeler")
elif lucas_points > dustin_points and lucas_points > eleven_points:
    print (f"you are most like lucas sinclair")
elif dustin_points > eleven_points:
    print (f" you are most like dustin henderson")
elif eleven_points:
    print (f"you are most like eleven hopper")
    print ("ᯓ★ˎˊ˗")