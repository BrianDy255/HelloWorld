print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

start = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'\n")

if start == 'left':
    swim_or_wait = input("Would like to continue forward and 'swim' to the next destination or 'wait'?\n")
    if swim_or_wait == "swim":
        print("Attacked by trout. GAME OVER!")
    else:
        which_door = input("You come across a corridor that has 3 doors: 'Red', 'Blue', or 'Yellow'. Which"
                           " door will you choose?\n").lower()
        if which_door == "red":
            print("Burned by fire. Game OVER!")
        elif which_door == 'blue':
            print("Eaten by monsters. GAME OVER!")
        elif which_door == "yellow":
            print("YOU WIN!")
        else:
            print("Game OVER!")
else:
    print("You fell into a hole. Game over!")
