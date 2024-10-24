import random

def name_to_number(name):
    if(name == paper):
        number = 1
    elif(name == scissors):
        number = 2
    elif(name == rock):
        number = 3
    return number

def number_to_name(number):
    if(number == 1):
        name = "paper"
    elif(number == 2):
        name = "scissors"
    elif(number == 3):
        name = "rock"
    return name
player_choice = input("rock, scissors or paper")
def play(player_choice):
    comp_choice = random.randint(1,3)
    if (player_choice == "paper"):
        if(comp_choice == 1):
            print("tie")
        if(comp_choice == 2):
            print("you lost")
        if(comp_choice == 3):
            print("you won")
    if (player_choice == "scissors"):
        if(comp_choice == 1):
            print("you won")
        if(comp_choice == 2):
            print("tie")
        if(comp_choice == 3):
            print("you lost")
    if (player_choice == "rock"):
        if(comp_choice == 1):
            print("you lost")
        if(comp_choice == 2):
            print("you won")
        if(comp_choice == 3):
            print("tie")
    print("computer chose:")
    print number_to_name(comp_choice)
    
play(player_choice)
        
        
        
