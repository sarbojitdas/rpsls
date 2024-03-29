# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if (name=="rock"):
        return 0
    elif(name=="spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4
    else:
        return "wrong choice"


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if(number==0):
        return "rock"
    elif(number==1):
        return "spock"
    elif(number==2):
        return "paper"
    elif(number==3):
        return "lizard"
    elif(number==4):
        return "scissors"
    else:
        return "wrong choice"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    pass
    
    # print a blank line to separate consecutive games
    print()

    # print out the message for the player's choice
    print("player's choice",player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number=name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)
    
    # print out the message for computer's choice
    print("computer's choice",comp_choice)
    # compute difference of comp_number and player_number modulo five
    difference=(comp_number-player_number)

    # use if/elif/else to determine winner, print winner message
    if(difference==0):
       print("player and computer tie")
    elif(difference==1)or(difference==2):
        print("computer wins")
    else:
        print("player wins")
        

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


