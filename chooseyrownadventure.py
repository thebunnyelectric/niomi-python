#Choose Your Own Adventure - attempt 1 - Niomi Hill
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
print('''
Welcome to Treasure Island
Your mission is to find the treasure.
''')
choice1 = input("You wake up in a strange place and don't know where you are or how you got there. \n \nTo your right is a dilapidated mansion overgrown with vines. \n \nTo your left is a path to what appears to be a beach with a boat tied to a dock. \n \nYou're not sure if you should go into the mansion and seek shelter for the night, or head to the boat and try to leave this strange place as soon as possible. \n \nDo you go right to enter the mansion or go left down the path to the boat? Enter 'Left' or 'Right'" )
if choice1 == "right" or choice1 == "Right":
    print("You decide and enter the mansion to seek shelter for the night. \n \nYou take 3 steps and realize too late the floorboards are rotted and can't hold your weight. \n \nYou fall through the floor to the basement below and are impaled through the heart by a piece of old lumber. You die within minutes. \n \nGame over. ")
elif choice1 == "left" or choice1 == "Left":
    choice2 = input("You decide to turn left and walk down the path to the dock to examine the boat. \n \nThe boat looks sturdy enough but the tide is low and you won't be able to leave until it rises again in the evening, which is hours from now. \n \nYou see some cottages on an island not too far from the dock and the water looks calm enough to swim safely. \n \nDo you wait for high tide so you can take the boat or save yourself hours of time and swim across to the island? Enter 'Boat' or 'Swim' ")
    if choice2 == "Swim" or choice2 == "swim":
        print("The water looks safe so you decide to swim to the cottages on the island. \n \nBy the time you're chest deep in the water and start to swim to the island, you're suddenly swarmed by a school of hungry piranhas. \n \nYou can't escape their ferocious teeth and quickly succomb to their bloodlust. \n \nGame over.")
    elif choice2 == "Boat" or choice2 == "boat":
        choice3 = input("You decide to wait for high tide so you can take the boat to the cottages on the island. \n \nYou steer the boat over to the island and it handles well, before you know it you've reached the shore. \n \nYou drag the boat onto the sand and head off towards the cottages. \n \nOnce you get close to the cottages you see there are 3 in a row, each with a different colour door. \n \nThe first cottage has a yellow door, the second cottage has a blue door, and the third cottage has a red door. \n \nWhich door do you choose? Enter 'Yellow', 'Blue', or 'Red' " )
        if choice3 == "Red" or choice3 == "red":
            print("You approach the cottage with the red door and open it. \n \nYou enter the cottage and too late, notice a large black bear a couple of feet away from you. \n \nThe bear eats you alive. Oh no! Game over." )
        elif choice3 == "Blue" or choice3 == "blue":
            print("You walk up to the cottage with the blue door and open it. \n \nYou take several steps into the cottage and notice the beautiful decor. \n \n The cottage is so lovely, seems safe, and you're exhausted so you sit down on an ornate beautifully carved kitchen table. \n \nYou lay your head down on your arms at the kitchen table and fall asleep. \n \nUnfortunately there's a gas leak and you succomb to carbon monoxide poisining. How sad. Game over." )
        elif choice3 == "Yellow" or choice3 == "yellow":
            print("You carefully approach the cottage with the yellow door and open it. \n \nYou peer inside the cottage, it's well lit even with the evening sun and seems safe enough to enter. \n \nYou walk into the cottage to investigate and see a room off to the side. \n \nYou take a few steps inside the room and notice a large ornate chest with a heavy lock. \n \nYou go back inside the main room of the cottage and grab an iron poker by the fireplace and go back to the chest. \n \nYou swing the iron poker as hard as you can and WHAM! crack open the lock on the first try. \n \nInside the chest is a treasure trove of gold coins and jewels. You're amazed and relieved because it looks like you'll never have to work another day in your life. Holy cow! You win!" )
        else:
            print("Wrong choice. Game over")
    else:
        print("Wrong choice. Game over")
else:
    print("Wrong choice. Game over")