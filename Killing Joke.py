def intro():
    print("You arrive at Arkham Asylum")
    print("You head to cell number 0801 to talk to the joker")
    print("You choose to 'enter' or 'go home'")

    choice = input('> ')

    if choice == "enter":
        print("You enter and sit opposite the Joker")
        talk_to_joker()
    else:
        game_over("You returned to the Batcave")

def game_over(end):
    print(end, "Game over")
    exit(0)

def talk_to_joker():
    print("You came to talk but realised he was an imposter")
    print("You make one of the following decisions:'interrogate', kill', or 'play cards'")
    
    choice = input('> ')

    if choice == "interrogate":
        print("You get a clue on Jokers location")
        print("You find out he shot barbra and kidnapped Gordon")
        barbra()
    elif choice == "kill":
        print("Batman doesn't kill")
        game_over("You blew it!")
        exit(0)
    elif choice == "play cards":
        print("what? are you a nurse? try again")
        talk_to_joker()
    else:
        game_over("learn to follow instructions.")

def barbra():
    print("She tells you where the Joker took Gordan")
    print("You type one of the following: \n 1. ignore her \n 2. listen to her.")
    go_to_gordan = False
    while True:
        
        choice = input('> ')

        if choice == "ignore her":
            game_over("why ignore her?")
        elif choice == "listen to her" and not go_to_gordan:
            print("You go to the amusment park")
            go_to_gordan = True
            Amusment_park()
        else:
            print("You have to pick one of the options") 

def Amusment_park():
    print("You free Gordan and chase after the Joker")
    print("You either go \"left\" or \"right\"")

    choice = input('> ')

    if "left" in choice:
        print("Congrats! you capture the Joker")
        exit(0)
    elif "right" in choice:
        game_over("You fall and die in a pit of spikes")
        exit(0)
    else:
        print("You have to print 'left' or 'right'")


intro()