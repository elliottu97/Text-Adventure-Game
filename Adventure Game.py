#Interactive Fiction Adventure Game
#CMPS 5P
#David Lenci, Cole Malinowski, Antonio Guerrero, Elliot Tu


import time as t #Used in wait function
import random as r #Used in cave function as possible story line
atmpts = 1
def win():
    print("""You feel the ground shaking beneath your feet, and hear the sounds of rocks falling in the cave. 
    Just as you are being consumed by the rock you wake up. It was just a dream.""")
    agn = str(input('Would you like to play again?yes[1] or no[2]'))
    if agn == 1:
        return text_adventure()
    if agn == 2:
        print('Thanks for playing!')
def stuck():
        print("You try with all your strength but the door wont budge, and the lock holds true.")
        dec1 = input(str("What would you like to do? Try again [1] or Inspect the Writing [2]"))
        if dec1 == 1:
            return stuck() #The door won't open on mere strength alone
        if dec1 == 2:
            return unstuck()

def unstuck():
    print("The words read 'This lock needs 3 numbers to open. 27//5 , 32%6 , len(blizzard)'")
    cc = list(input("Please enter the three digit code"))
    print(cc)
    for i in cc:
        if i != '5' and i != '2' and i != '8': #User must enter all three correct numbers in order to move on
            print("That number is incorrect")
            return unstuck() #If the user answers incorrectly, the question will be asked again
        else:
            print('That code is correct. The door opens to a blinding light and you wake up in your room. It was all a dream')

def door():
    x = input(str('''You arrive at a sturdy wooden door secured by an old combination lock.
    You can see there are some words inscribed on the door.
    What would you like to do? Try to open the door [1] or Inspect the writing [2]'''))

    if x == '1':
        print(stuck())
    if x == '2':
        print(unstuck())


def text_adventure():
    print('''You wake up in a cave. You have no idea how you got there. Outside there is a severe snowstorm.
    To your left their is a brown backpack. Inside there is a Knife, food , and a torch. You grab the backpack.''')
    Inventory = ['Knife', ['food', 2], 'Torch']
    drct = input(str('Where would you like to go? In to the cave[1] or Out of cave[2]'))
    if drct == 'nothing':
        print(wait())
    if drct == '1': #entering cave
        print(cave())
    if drct == '2': #leave cave - player can't win
        print(leave())


def leave():
    a = input(str('''You walk out of the cave, and are surrounded by snow in all directions.
    In the distance you make out what appears to be a path in the snow.
    Would you like to go to it? yes[1] or no[2]?: '''))

    if a == '1':
        print('''You walk to the path where you see a pole with a sign on it. As you try to read the sign you here
        a sound. The last thing you see are two lights moving quickly at you.''')
        print(text_adventure())

    if a == '2':
        b = input(str(''''You continue to look around, but all you see is snow.
        Would like to return to the cave? yes(1) or no(2)?:'''))
        if b == '1':
            c = input(str('''You return to the cave. Where would you like to go?
            In to the cave[1] or leave the cave[2].'''))
            if c == '1':
                print(cave())
            if c == '2':
                print(leave())
            if c == 'nothing':
                print(wait())
        elif b == '2':
            print('''As you wait you pass out from hypothermia.''')
            print(text_adventure())

    else:
        print('''As you wait you pass out from hypothermia.''')
        print(text_adventure())


def wait(): #Easy way to win if player enters correct input.
    t.sleep(10)
    a = input(str('''After waiting a few hours the snow storm stops.
    Would you like to leave? yes(1) or no (2):'''))
    if a == 1:
        print('''You walk outside and see a road in the distance.
        You walk to it where a truck driver sees you and pulls over.
        He yells out the window "Need a ride?"
        You nod your head and jump in the truck.
        The driver glances at you, "You look you had a rough night. Let me guess finals?"
        You both start chuckling as you continue down the road.''')
        a = input(str('Would you like to play again? yes(1) or no(2):'))


        if a == '1':
            print(text_adventure())
        if a == '2':
            print('Thank you for playing!')

def text_adventure2(i):     #'''Recursion to ensure players beat the game by their third try.
                            # Includes copy of cave function and the winning cave function.'''

    def cave2():
        print("You proceed into a dark cave")
        x = input("There are two pathways. Enter [1] for right and [2] for left")
        if x == "1":
            print("""You chose to go to the right and fall, there is no going back.
            The path continues onward, but you notice a small hole to your right.
            What would you like to do? Enter [1] to continue forward and [2] to enter the small hole.""")
            x = input("Enter [1] or [2]")
            if x == "1":
                print("""You chose to continue down the path.
                After walking for 3 minutes you come across two doors.
                One door has a Trefoil symbol on it while the other is blank.
                What would you like to do? Enter [1] to open the door with the Trefoil symbol on it or
                [2] to open the blank door.""")
                x = input("Enter [1] or [2]")
                if x == "1":
                    print("""Upon entering the room you are knocked out by a masked individual.""")
                    return text_adventure2(i)
                if x == "2":
                    print("The door is locked, you walk back to where you started.")
                    return text_adventure2(i)
            if x == "2":
                print("""You chose to enter the small hole.
                You notice a hidden ladder and s small creek.
                What would you like to do? Enter [1] to climb down the hidden ladder or
                [2] to follow the river.""")
                x = input("Enter [1] or [2]")
                if x == "1":
                    print("""You climb down the ladder, people seem to be living here.
                          As you turn around to leave one of them says "If it is victory you seek lucky you must be"
                          A grin appears on his face as he states"Guess how many fingers I am holding behind my back." """)
                    gss = str(input("Assuming he has five fingers enter in your guess:"))
                    fgrs = r.randrange(1, 6)
                    if gss == fgrs:
                        print('''The grin on his face fades, "You are correct traveler, what you are looking for is behind this door."
                        You enter through the door.''')
                        return win()
                    else:
                        print('''The grin on his face grows wider as he reveals he actually had''', fgrs,'''behind his back.
                        The man pulls out a dagger and chases you back the way you came.''')
                        return text_adventure2(atmpts)
                if x == "2":
                    print("""As you are following the river a swarm of bats forces you to run back
                     to the beginning of the cave""")
                    return text_adventure2(i)
        elif x == "2":
            print("""You went to the Left. There is a small passage way in front of you, and a waterfall to your left.
             Would you like to crawl through the passage way [1], or inspect the waterfall [2]?""")
            x = input("Enter [1] or [2]")
            if x == "1":
                print("""After squeezing through the small hole. You walk into a large open space. 
                On the far end of the cave there is a rock wall,
                 and right next to you the cave starts to slope downwards.
                 Would you like to climb the wall [1], or continue down the cave [2]?""")
                x = input("Enter [1] or [2]")
                if x == "1":
                    print("""You barely make it up the wall to see that it is a dead end; heartbroken, you proceed to the entrance of the cave.""")
                    return text_adventure2(i)
                if x == "2":
                    print("""You continue down the cave, 
                    after a few minutes your lantern flickers and dies out, you blindly find your way back to the beginning of the cave """)
                    return text_adventure2(i)
            if x == "2":
                print(str("""Upon further inspection of the waterfall you find a passage way behind it.
                It seems to be man-made. What would you like to do? 
                Head back because you do not know what will go on there [1] or go down the passageway [2]? """))
                x = input("Enter [1] or [2]")
                if x == "1":
                    print("You turn around and run back to the entrance of the cave")
                    return text_adventure2(i)
                if x == "2":
                    door()
                    return win()


    def winning_cave(): #Function players are forced down on their third attempt.
        print('Winning cave function')
        print("You proceed into a dark cave")
        x = input("There are two pathways. Enter [1] for right and [2] for left")
        if x == "1":
            print("""You chose to go to the right and fall, there is no going back.
            The path continues onward, but you notice a small hole to your right.
            What would you like to do? Enter [1] to continue forward and [2] to enter the small hole.""")
            x = input("Enter [1] or [2]")
            if x == "1":
                print("""You chose to continue down the path.
                After walking for 3 minutes you come across two doors.
                One door has a Trefoil symbol on it while the other is blank.
                What would you like to do? Enter [1] to open the door with the Trefoil symbol on it or
                [2] to open the blank door.""")
                x = input("Enter [1] or [2]")
                if x == "1":
                    print("""Upon entering the room you are knocked out by a masked individual. 
                    When you regain consciousness you are experiencing an earthquake.""")
                    return win()
                if x == "2":
                    print("The door is locked, you begin to walk back to where you started until ")
                    return win()
            if x == "2":
                print("""You chose to enter the small hole.
                You notice a hidden ladder and s small creek.
                What would you like to do? Enter [1] to climb down the hidden ladder or
                [2] to follow the river.""")
                x = input("Enter [1] or [2]")
                if x == "1":
                    print("""You climb down the ladder, people seem to be living here.
                          They chase you to the beginning of the cave. During the chase you begin to feel the foreshocks of a large earthquake.""")
                    return win()
                if x == "2":
                    print("""As you are following the river a swarm of bats forces you to run back
                     to the beginning of the cave. After sitting right inside the entrance of the cave for a few minutes """)
                    return win()
        elif x == "2":
            print("""You went to the Left. There is a small passage way in front of you, and a waterfall to your left. 
            Would you like to crawl through the passage way [1], or inspect the waterfall [2]?""")         #You should only have to fill in the ... to complete the story,
            x = input("Enter [1] or [2]")
            if x == "1":
                print("""After squeezing through the small hole. You walk into a large open space. 
                On the far end of the cave there is a rock wall, and right next to you the cave starts to slope downwards.
                 Would you like to climb the wall [1], or continue down the cave [2]?""")
                x = input("Enter [1] or [2]")
                if x == "1":
                    print("""You barely make it up the wall to see that it is a dead end; heartbroken, you proceed to the entrance of the cave. Luckily you headed back when you did because at the entrance """)
                    return win()
                if x == "2":
                    print("""You continue down the cave, after a few minutes your lantern flickers and dies out, you blindly find your way back to the beginning of the cave just as """)
                    return win()
            if x == "2":
                print(str("""Upon further inspection of the waterfall you find a passage way behind it.
                It seems to be man-made. What would you like to do? 
                Head back because you do not know what will go on there [1] or go down the passageway [2]? """))
                x = input("Enter [1] or [2]")
                if x == "1":
                    print("You turn around and run back to the entrance of the cave before ")
                    return win()
                if x == "2":
                    door()
                    return win()
    l = str(input('''You end up at the cave entrance again what would you like to do? 
    Enter 1 to leave the cave or enter 2 to go back into the cave.'''))
    attmpts = i + 1  #players can only win if they enter the cave or type in the easteregg
    if l == '1':
        print(leave())
    elif l == 'nothing':
        print(wait())
    elif l == '2':
        if atmpts < 3:
            return cave2()
        elif atmpts >= 3:
            return winning_cave()



def cave(): #'''This is the function that will be called the first time the player enters the cave.
            #  Every other time will be in text_adventure2()'''
    print("You proceed into a dark cave")
    x = input("There are two pathways. Enter [1] for right and [2] for left")
    if x == "1":
        print("""You chose to go to the right and fall, there is no going back.
        The path continues onward, but you notice a small hole to your right.
        What would you like to do? Enter [1] to continue forward and [2] to enter the small hole.""")
        x = input("Enter [1] or [2]")
        if x == "1":
            print("""You chose to continue down the path.
            After walking for 3 minutes you come across two doors.
            One door has a Trefoil symbol on it while the other is blank.
            What would you like to do? Enter [1] to open the door with the Trefoil symbol on it or
            [2] to open the blank door.""")
            x = input("Enter [1] or [2]")
            if x == "1":
                print("""Upon entering the room you are knocked out by a masked individual.""")
                return text_adventure2(atmpts)
            if x == "2":
                print("The door is locked, you walk back to where you started.")
                return text_adventure2(atmpts)
        if x == "2":
            print("""You chose to enter the small hole.
            You notice a hidden ladder and s small creek.
            What would you like to do? Enter [1] to climb down the hidden ladder or
            [2] to follow the river.""")
            x = input("Enter [1] or [2]")
            if x == "1":
                print("""You climb down the ladder, people seem to be living here.
                      As you turn around to leave one of them says "If it is victory you seek lucky you must be" 
                      A grin appears on his face as he states"Guess how many fingers I am holding behind my back." """) # Here is where we use random
                gss = str(input("Assuming he has five fingers enter in your guess:"))
                fgrs = r.randrange(1, 6)
                if gss == fgrs:
                    print('''The grin on his face fades, "You are correct traveler, what you are looking for is behind this door."
                    You enter through the door.''')
                    return win()
                else:
                    print('''The grin on his face grows wider as he reveals he actually had''', fgrs,'''behind his back.
                    The man pulls out a dagger and chases you back the way you came.''')
                    return text_adventure2(atmpts)
            if x == "2":
                print("""As you are following the river a swarm of bats forces you to run back
                 to the beginning of the cave""")
                return text_adventure2(atmpts)
    elif x == "2":
        print("""You went to the Left. There is a small passage way in front of you, and a waterfall to your left.
         Would you like to crawl through the passage way [1], or inspect the waterfall [2]?""")
        x = input("Enter [1] or [2]")
        if x == "1":
            print("""After squeezing through the small hole. You walk into a large open space. On the far end of the cave there is a rock wall,
             and right next to you the cave starts to slope downwards.
             Would you like to climb the wall [1], or continue down the cave [2]?""")
            x = input("Enter [1] or [2]")
            if x == "1":
                print("""You barely make it up the wall to see that it is a dead end; heartbroken, you proceed to the entrance of the cave.""")
                return text_adventure2(atmpts)
            if x == "2":
                print("""You continue down the cave, 
                after a few minutes your lantern flickers and dies out, you blindly find your way back to the beginning of the cave """)
                return text_adventure2(atmpts)
        if x == "2":
            print(str("""Upon further inspection of the waterfall you find a passage way behind it.
            It seems to be man-made. What would you like to do? 
            Head back because you do not know what will go on there [1] or go down the passageway [2]? """))
            x = input("Enter [1] or [2]")
            if x == "1":
                print("You turn around and run back to the entrance of the cave")
                return text_adventure2(atmpts)
            if x == "2":
                door()
                return win()


print(text_adventure())
