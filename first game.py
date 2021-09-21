print("You're a passenger of a ship that sank near a beautiful tropical island. After reaching the beach you look around and decide on one of three options. Type 1 if you 'set a fireplace', type 2 if you 'sit down and cry', type 3 if you 'go to the jungle to get some food'")
print()
playerChoice = input("Type the number of your decision:")
if playerChoice == "1":
    print("In the evening you get noticed by local animals. A friendly monkey approaches you. What do you do?")
    print("You can: >(1) pet her. You are an animal lover!, (2) leave her alone. It's a wild animal though.")
    print()
    playerChoice2 = input("Type the number of your decision:")
    if playerChoice2 == "1":
        print("The monkey allows you to pet her and you get a brilliant idea that she has to be domesticated. You follow the monkey to the nearest village.")
        print("YOU ARE SAVED!")
    elif playerChoice2 == "2":
        print("You regret not having your phone with you and you can't make a selfie with a cute monkey. It makes you crazy.")
        print("It's time to reveal the truth. Someone or some computer finally has to tell it...")
        print("YOU ARE INSANE! GAME OVER!")
    else:
        print("Sorry, you didn't enter 1 or 2")
        print("Run the game again to have another go.")
elif playerChoice == "2":
    print("You can hear a noise in the bushes. It's you best friend laughing hard because you got fooled and it's just a good prank!")
    print("Just kidding.")
    print("You're probably going to DIE really soon...")
elif playerChoice == "3":
    print("You're exploring the forest, but in a quarter you notice a tiger sneaking around!")
    print("Focus! Here's what you can do: (1) grab a stone and a stick and get ready for a fight, (2) climb a tree as a monkey and just wait...")
    playerChoice3 = input("Type the number of your decision:")
    if playerChoice3 == "1":
        print("The tiger defeats you in seconds. He eats you. You're delicious!")
        print("GAME OVER!")
    elif playerChoice3 == "2":
        print("You get noticed by a group of scientists observing the tiger. YOU ARE SAVED!")
        print("CONGRATULATIONS!")
    else:
        print("Sorry, you didn't enter 1 or 2")
        print("Run  the game again to have another go.")
else:
        print("Sorry, you didn't enter 1, 2 or 3")
        print("Run the game again to have another go.")
print("THE END")



    
