"""
- Escape Room Simulator: Different drawn out items in Python turtle or maybe even use ASCII art
    and there is a menu to choose from different options similarly to a role-playing game (RPG) 
    but really advanced with an inventory and different elements included. (Eg. Success rate based 
    on option choices, inventory, hints/clues, timelimit, different breakout rooms)
"""
import turtle
import time
import random as r
import os

#For numbers of the clock
pen = turtle.Turtle()
pen.hideturtle()
pen.speed("fastest")

print("Welcome to Escape Sequence! You have 10 minutes to escape.")
time.sleep(1)
print("""
In this escape room game, there are limits to what you are able to do:\n 
1. Please do not crash the game in any way \n 
2. Don't interact with anything on the turtle screen \n 
3. Choose the options prompted by the number, not the word.\n
4. Have fun!
""")
time.sleep(3)


# Draw room
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
 
def fill_poly(t, points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()
 
def draw_poly(t, points, color="#5a4a3a", width=1):
    t.pensize(width)
    t.pencolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
 
def draw_line(t, p1, p2, color="#5a4a3a", width=1):
    t.pensize(width)
    t.pencolor(color)
    t.penup()
    t.goto(p1)
    t.pendown()
    t.goto(p2)

def ellipse(rad):
  # rad --> radius of arc
  for i in range(2):
    # two arcs
    t.circle(rad,90)
    t.circle(rad//2,90)


# Room geometry (centered, turtle coords: origin = center of screen)
# Outer corners
TL = (-400, 320)   # top-left
TR = ( 400, 320)   # top-right
BL = (-400,-270)   # bottom-left
BR = ( 400,-270)   # bottom-right
 
# Inner back-wall corners (vanishing box)
IL = (-120, 60)
IR = ( 120, 60)
ILB = (-120,-90)
IRB = ( 120,-90)
 
# Fill panels 
fill_poly(t, [TL, TR, IR, IL],       "#e2ddd8")  # ceiling
fill_poly(t, [IL, IR, IRB, ILB],     "#d6cfc4")  # back wall
fill_poly(t, [TL, IL, ILB, BL],      "#bfb8ae")  # left wall
fill_poly(t, [TR, IR, IRB, BR],      "#c9c2b7")  # right wall
fill_poly(t, [BL, ILB, IRB, BR],     "#a89070")  # floor
 
 
# Window on back wall 
wx, wy, ww, wh = -60, 35, 120, 95

 
# Window frame
fill_poly(t, [(wx, wy), (wx+ww, wy), (wx+ww, wy-wh), (wx, wy-wh)], "#c5b89a")
# Glass panes
for gx, gy, gw, gh in [
    (wx+5,  wy-5,  52, 40),
    (wx+5,  wy-50, 52, 40),
    (wx+63, wy-5,  52, 40),
    (wx+63, wy-50, 52, 40),
]:
    fill_poly(t, [(gx,gy),(gx+gw,gy),(gx+gw,gy-gh),(gx,gy-gh)], "#b8d8e8")
 
# Window outer frame border
draw_poly(t, [(wx,wy),(wx+ww,wy),(wx+ww,wy-wh),(wx,wy-wh)], "#5a4a3a", 2)

#Objects

#Door
fill_poly(t, [(-350, -225), (-287, -184.5), (-287, 175), (-350, 225)], "#8B4513") 
t.penup()
t.goto(-305,-10)
t.color("DarkGoldenrod2")
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.color("black")
t.circle(10)
t.penup()

#Rug
fill_poly(t, [(-120,-250), (120,-250), (100, -120), (-100, -120)], "#BBB791")
fill_poly(t, [(-110,-240), (110,-240), (90, -130), (-90, -130)], "#90D5FF")
t.penup()

#Clock
t.goto(-250, 20)
t.color("AliceBlue")
t.pendown()
t.setheading(315)
t.begin_fill()
ellipse(35)
t.end_fill()
t.color("black")
ellipse(35)
t.penup()
t.goto(-251,19)
t.pendown()
t.color("black")
ellipse(36)
t.penup()
t.goto(-251,20)
t.pendown()
t.color("black")
ellipse(36)
t.penup()

#Draw the hands
t.goto(-225, 30)
t.pendown()
t.goto(-215, 35)
t.penup()
t.goto(-225, 30)
t.pendown()
t.goto(-232, 50)
t.penup()

#Draw the Numbers on Clock
clockFont = ("Space Grotesk",12,"normal") #Font 12 for mac, spacegrotesk font
pen.penup()
pen.goto(-208, 26)
pen.pendown()
pen.write(3, font=clockFont)
pen.penup()
pen.goto(-226, 11)
pen.pendown()
pen.write(6, font=clockFont)
pen.penup()
pen.goto(-248, 25)
pen.pendown()
pen.write(9, font=clockFont)
pen.penup()
pen.goto(-228, 38)
pen.pendown()
pen.write(12, font=clockFont)
pen.penup()

#Trashcan
t.color("black")
t.goto(250, -220)
t.pendown()
t.goto(250, -250)
t.color("#d4d6d9")
t.begin_fill()
t.end_fill()
t.color("black")
t.goto(278, -220)
t.penup()
t.goto(250, -220)
t.right(90)
t.pendown()
t.color("black")
t.left(90)
t.circle(20, 90)
t.left(90)
t.circle(20, 90)
t.penup()
fill_poly(t, [(250, -220), (250,-250), (278, -250), (278, -220)], "#d4d6d9")

#Table
fill_poly(t, [(-100,-190), (100,-190), (80, -70), (-80, -70)], "#472e18")


#----------------------------------------------------------------------
#First room
# Unscramble the word to move on, objects include:
# door - !
# table - paper under one of the legs has letter 'a'
# plant - !
# clock - different riddle for second 'e'
#    - "I am the beginning of eternity, the end of time and space, the beginning of every end, and the end of every place. What am I?"
# window - !
# rug - under rug has letter 's'
# dishes - clue to 'c' with first letter of every dish
# trash can - !
# chair - !
# shoes - in the shoes, clue to rug
#   - This item is made from 100% real fur
# lamp - turn on to reveal letter 'p'
# envelope - riddle to get letter 'e' 
#   - What starts with an E, ends with an E, but only contains one letter?" The answer is an envelope,
#----------------------------------------------------------------------

#timer
totalTime=600
start = time.time()

# Make loop to see what user interacts with
while True:
    end = time.time()
    timer = end-start
    timer = timer//1

    if timer > totalTime:
        print("Times up! You lose, womp womp!")
        quit()

    print("\n\n\nWhat would you like to interact with?")
    print("Options:\n1. Door\n2. Table\n3. Plant\n4. Clock\n5. Window\n6. Rug\n7. Dishes\n8. Trash can\n9. Chair\n10. Shoes\n11. Lamp\n12. Envelope\n13. Door Lock")
    choice = input("> ")
    #Door
    if choice == "1":
        print("Why did the door go to the therapist?")
        time.sleep(3)
        print("Because it had a problem opening up!")
    #Table
    elif choice == "2":
        print("Hmm, there is nothing suspicious about the table, but the table leg seems loose. Should we check it out?\n1. Yes\n2. No")
        tableLeg = input("> ")
        if tableLeg == "1":
            print("There was a letter a carved on the top of the table leg! Letter: a")

    #Plant
    elif choice == "3":
        print("Why are trees such good cheerleaders? ")
        time.sleep(3)
        print("They are always rooting for you!")
        time.sleep(3)
        print("Why did the tomato turn red?")
        time.sleep(3)
        print("Because it saw the salad dressing!")
        time.sleep(3)
        print("Hey I'm jubilent Jokey, you should really move on now. You know, I am only here for the jokes, but the time is ticking! ")
    #Clock
    elif choice == "4":
        print("There is a little piece of paper wedged in the hands of the clock. Let's see what it says.")
        time.sleep(4)
        print("I am the beginning of eternity, the end of time and space, the beginning of every end, and the end of every place. What am I?")
    #Window
    elif choice == "5":
        print("The view outside is breathtaking! Look at those...")
        time.sleep(4)
        print("Oh, its just wallpaper")
    #Rug
    elif choice == "6":
        print("It seems like there is a hot-iron branding of the letter S under the back corner of the rug. Interesting.")
    #Dishes
    elif choice == "7":
        print("There's a bunch of food on the table...")
        time.sleep(2)
        print("There's Caviar, Curry, a Can of Coke, Chicken, Carbonara buldak,")
        print("Cooked Cabbage, Chocolate Cake, and even some Congee jelly.")
        print("yum, some tasty hints...")

    #Trash can
    elif choice == "8":
        print("Remember to never liter! $1000 fine just for not using ME to your advantage.")
    #Chair
    elif choice == "9":
        print("Such a nice polished wooden chair. Wow! It's actually an antique that Isaac Newton carved when he was in school for wood working class! How cool.")
    #Shoes
    elif choice == "10":
        print("The item you should be looking for is made from 100 percent real fur.")
    #Lamp
    elif choice == "11":
        print("This lamp seems to be plugged in. Should we turn it on?\n1. Yes\n2. No")
        lampLight = input("> ")
        if lampLight == "1":
            print("There was a letter p illuminated on the bulb of the lamp.")
    #Envelope
    elif choice == "12":
        print("What starts with an E, ends with an E, but only contains one letter?") 
        time.sleep(5)
        print("The answer is an envelope.")
    #Door Lock
    elif choice == "13":
        print("Did you uncover all of the missing letters? Let's try your luck!")
        answer = input("> ")
        if answer == "escape":
            print("The lock actually opened!")
            print("Interesting, you managed to make it past Level 1. Congrats. Congrats for wasting so much time! HAHahaha")
            break
        else:
            print("INCORRECT, MWAHAHAHAHAH. You better pay closer attention to the hints! Remember time is ticking!")    

    #time to read
    time.sleep(2)


#Level 2
"""
Trivia Level
User has to answer 10 questions 
there will be 20-30 possible questions
Each wrong answer takes 3 seconds from their time
Once they get all 10, they move on

Questions will be multiple choice (A,B,C)
Will include general knowledge
"""

questions = [
    "What is the highest mountain in the world, in terms of elevation?", #Mauna Kea
    "What do you call a fake noodle?", #An impasta
    "If you throw me out the window, you will leave a grieving wife. Bring me back, but in the door, and you'll see someone giving life. What am I?", #The letter N
    "What's so fragile that saying it's name breaks it?", #silence
    "This thing all things devours: birds, beasts, trees, flowers; gnaws iron, bites steel; grinds hard stones to meal; slays king, ruins town, and beats high mountain down. What is it?", #Time
    "The more you take, the more you leave behind. What am I?", #Footsteps
    "I am an odd number. Take away a letter and I become even. What number am I?", #Seven
    "I travel around the world, but I stay in a  corner.", #Postage Stamp
    "In what year were the first Winter Olympic Games held?", #1924
    "Which city gave its name to a culinary specialty consisting of cooking a fillet of beef in puff pastry stuffed with foie gras?",
      #Wellington
    "Which of the following is NOT a fruit?" #Rhubarb

]

print("Welcome to level 2. ")
time.sleep(.5)
print("For this level, you must answer 10 questions correct")
time.sleep(2)
print("IF you answer a question incorrectly 3 seconds will be taken from your time.")
time.sleep(2)
print("Good luck! Remember the clock is ticking.")
time.sleep(1)


correct = 0
#Game loop for level 2
print("\nYour first question is...")
while correct<10:
    end = time.time()
    timer = end-start
    timer = timer//1

    if timer > totalTime:
        print("Times up! You lose, womp womp!")
        quit()
    time.sleep(2)
    
    cQuestion = r.randint(0,len(questions)-1) #pick a random question
    print("\n"+questions[cQuestion])
    if cQuestion==0:
        print("A. Mount Everest")
        print("B. Mauna Kea")
        print("C. Savage Mountain")
        print("D. K2")
        answer = str(input("> ")).upper()
        if answer=="A":
            print("Incorrect, please read the question carefully.")
            start-=3
        elif answer=="B":
            print("Correct! You are absolutely right! \nThe mountain is measured from the base, which is underwater. \nMount Everest would be the tallest mountain ABOVE sea level.")
            correct +=1
        elif answer=="C":
            print("He goes for the shot! It's up! But it is not good, he fails to make the crucial basket.")
            start-=3
        elif answer=="D":
            print("CLose enough of an answer, if this was on an actual test, I would have hoped you never signed up for the test in the first place.")
            start-=3
        else:
            print("Did you not understand the rules? You're supposed to type in a, b, c, or d...")
            start-=3
    if cQuestion==1:
        print("A. An impasta")
        print("B. An imposter")
        print("C. Kanoodle")
        print("D. A macaroni")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("Wooow, an intelligent human being. ")
            time.sleep(1)
            print("Your smarter than I thought, you seem to be unfoolable.")
            time.sleep(1)
            print("Or as Albert and Einstein say, shrewd and astute.")
            correct+=1
        if answer=="B":
            print("Fooled you!")
            time.sleep(1)
            print("You really think I would make the asnwer An impasta?")
            time.sleep(1)
            print("Oh, I guess it is. Good luck getting this question again ;D")
            start-=3
        if answer=="C":
            print("Tsk tsk tsk")
            time.sleep(1)
            print("Kanoodle is a game for little geniuses.")
            time.sleep(1)
            print("I know you want to be apart of their group, but better luck next time!")
            start-=3
        if answer=="D":
            print("Creamy, cheesy macaroni. Yum!")
            time.sleep(1)
            print("Oops, sorry, I thought I was muted.")
            time.sleep(1)
            print("Anyways, INCORRECT")
            start-=3

    if cQuestion==2:
            print("A. A surgeon")
            print("B. A hammer")
            print("C. The letter 'N'")
            print("D. A doctor")
            answer=str(input("> ")).upper()
            if answer=="A":
                print("Wrong")
                time.sleep(1)
                print("Incorrect")
                time.sleep(1)
                print("Miscalculated, perhaps")
                start-=3
            if answer=="B":
                print("Really! You think a hammer will bring you a grieving wife?")
                time.sleep(1)
                print("Actually your probably right, but not a door.")
                start-=3
            if answer=="C":
                print("You just got lucky that I, the creator of this game made Level two a multiple choice")
                time.sleep(1)
                print("If I made you answer the question by typing it out, you would have never passed.")
                time.sleep(1)
                print("MWWAAHAHAHAHAHHHAH")
                correct+=1
            if answer=="D":
                print("Nope, aaaaaand, there is three seconds gone from your time, again.")
                start-=3

    if cQuestion==3:
        print("A. Glass")
        print("B. Silence")
        print("C. An echo")
        print("D. Trust")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("Hard question, you tried your best though.")
            start-=3
        if answer=="B":
            print("Congrats! That is exactly the answer.")
            correct+=1
        if answer=="C":
            print("Well done, you answered incorreclty.")
            time.sleep(1)
            print("You know, I don't mind that answer, this was a difficult question.")
            start-=3
        if answer=="D":
            print("Yikes, Newton's got to watch out, because he might get run over by a false genius.")
            start-=3

    if cQuestion==4:
        print("A. Water")
        print("B. Time")
        print("C. Parabolas")
        print("D. T-Rex")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("That would be a correct 2nd answer, except its not the 1st correct answer. Sorry!")
            start-=3
        if answer=="B":
            print("Well done young prospect, you have excellently answered this simple riddle.")
            time.sleep(1)
            print("What will you go on to accomplish next?")
            correct+=1
        if answer=="C":
            print("Really, Parabolas?")
            time.sleep(1)
            print("Someone must really hate math class.")
            time.sleep(1)
            print("I wonder if you just hate it or if you had PTSD from a high school math teacher.")
            time.sleep(1)
            print("You know, the old lady Karen that doesn't give a crap about your questions or concerns on her teaching diploma.")
            time.sleep(2)
            print("Yeah, it was that bad.")
            start-=3
        if answer=="D":
            print("Although a T-Rex is pretty strong, it can't overcome the brutal force of humanity.")
            time.sleep(1)
            print("Wow, just thinking about all of humanity unitying, the armies, the airsupport, just like Jurassic Park.")
            time.sleep(1)
            print("Aside from the fact that the T-Rex dies!!            Sorry bud ;(")
            start-=3

    
    if cQuestion==5:
        print("A. Memories")
        print("B. Time")
        print("C. Food")
        print("D. Footsteps")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("Wrong, as simple as that.")
            start-=3
        if answer=="B":
            print("Hmm, close, but not quite.")
            start-=3
        if answer=="C":
            print("You must be hungry, but sorry, you're trying to escape not eat.")
            start-=3
        if answer=="D":
            print("Corrrrrrrreect! Fabulous work youngling. But you better hurry up, time is ticking!")
            correct+=1

    if cQuestion==6:
        print("A. Seven")
        print("B. sEvEn")
        print("C. seven")
        print("D. sEVEN")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("SEVEN!! Correct")
            correct+=1
        if answer=="B":
            print("INCORRECT, you better read the question carefully next time and see what it is asking for.")
            start-=3
        if answer=="C":
            print("SEVEN!! Correct")
            correct+=1
        if answer=="D":
            print("INCORRECT, please carefully read the question.")
            start-=3

    if cQuestion==7:
        print("A. Time Zones")
        print("B. Postage Stamp")
        print("C. O2")
        print("D. H2O")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("That would be correct if the question didn't specifically state, 'in the corner'.")
            time.sleep(1)
            print("And there is another 3 seconds away from your time, plus the time you are wasting trying to finish reading this.")
            time.sleep(1)
            print("Ha! Got you.")
            start-=3
        if answer=="B":
            print("A tremendous effort made by ")
            correct+=1
        if answer=="C":
            print("Really? Oxygen? You can come up with a better answer than that.")
            start-=3
        if answer=="D":
            print("psshh. You really need to get your game up buddy. Time is of the escence!")
            start-=3

    if cQuestion==8:
        print("A. 1954")
        print("B. 1890")
        print("C. 1924")
        print("D. 1974")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("WRONG")
            start-=3
        if answer=="B":
            print("HehEHeEHeHEHEhEHHEhEhhEEHEHEhEhEhEHHEhEhEHE, you got it WRONG")
            start-=3
        if answer=="C":
            print("Somebody really nailed history class in middle school. Continue...")
            correct+=1
        if answer=="D":
            print("IN -- IN ------ INC --------I N C O R R E C T ! !")
            start-=3

    if cQuestion==9:
        print("A. Washington")
        print("B. Wellington")
        print("C. Canberra")
        print("D. Dublin")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("It is important to recognize that the conclusion you reached is not supported by the logical progression of the argument. " \
            "While the answer may appear convincing at first glance, " \
            "a closer examination reveals several key factors that do not hold under scrutiny. " \
            "Being mistaken is a normal part of learning and problem-solving. " \
            "Revisiting the evidence step by step would likely reveal where the misunderstanding occurred and why the conclusion needs to be corrected.")
            start-=3
        if answer=="B":
            print("Wow, tricky question huh?")
            time.sleep(1)
            print("Congratulations.")
            correct+=1
        if answer=="C":
            print("There is no reasonable interpretation of the available evidence that supports the position you've taken. " \
            "The argument is fundamentally flawed because it relies on incorrect assumptions, overlooks critical facts, and reaches conclusions that simply do not follow from the evidence. " \
            "Every careful examination points to the same outcome: the claim is wrong. Continuing to defend it without addressing these issues only weakens the argument further. " \
            "A more careful review of the facts would make it evident that the correct conclusion is the exact opposite of the one being asserted.")
            start-=3
        if answer=="D":
            print("Your argument is incorrect, and the evidence does not support the conclusion you've drawn. " \
            "Every major point you've relied on has either been misinterpreted or applied in the wrong context, which causes the entire argument to fall apart. " \
            "There's nothing wrong with making mistakes—everyone does—but insisting on this conclusion despite the contradictory evidence would only move the discussion further away from the truth. " \
            "The most productive approach is to acknowledge the error and examine the facts again."
            "Please continue your dying effort")
            start-=3
            
    if cQuestion==10:
        print("A. Rumbatan")
        print("B. Rhubarb")
        print("C. Buddha's Hand")
        print("D. Snake Fruit")
        answer=str(input("> ")).upper()
        if answer=="A":
            print("MMMM, such a delicious vibrious red fruit. So delicious.")
            start-=3
        if answer=="B":
            print("Even though it does sound like rubber, it is not a fruit, it is a vegetable. Correct!")
            correct+=1
        if answer=="C":
            print("This was tricky, but I am playing mind games, go ahead, search up what Buddha's Hand is.")
            start-=3
        if answer=="D":
            print("It is an actual fruit believe it or not. Sorry!")
            start-=3

#End of level 2
print("Congrats! You actually managed to beat the two preestablished levels!\n You should be very glad that I did not have enough time to continue my game or else you definitely would have lost to my game.\n See you for another round of Escape Sequence!")


"""

"""


