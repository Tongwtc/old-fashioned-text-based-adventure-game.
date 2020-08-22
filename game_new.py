import time
import random


def print_pause(message):
    print (message)
    time.sleep(1)


def check_valid(choice):
    while True:
        if choice == "1":
            break
        elif choice == "2":
            break
        else:
            choice = input("(Please enter 1 or 2).")
    return choice


def intro(villain):  # introduction
    print_pause("You find yourself standing in an open field, \
    filled with grass and yellow wildflowers.")
    print("Rumor has it that a ", villain, "is somewhere around here, ")
    print_pause("and has been terrifying the nearby village")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty \
    (but not very effective) dagger.")


def fight(items, villain):
    # Things that happen when the player fights
    if "Sword of Ogoroth" in items:
        print("As the ", villain, "moves to attack, ")
        print_pause("you unsheath your new sword.")
        print_pause("Sword of Ogoroth shines brightly in your hand \
        as you brace yourself for the attack.")
        print_pause("But the gorgon takes one look at \
        your shiny new toy and runs away!")
        print("You have rid the town of the", villain, ".")
        print_pause("You are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print("but your dagger is no match for the ", villain)
        print_pause(" ")
        print_pause("You have been defeated!")
        play_again()


def cave(items, villain):
    # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")
    if "Sword of Ogoroth" in items:
        print_pause("You've been here before, and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")

    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and \
        take the sword with you.")
        items.append("Sword of Ogoroth")
    print_pause("You walk back out to the field.")
    choosing_field(items, villain)


def field(items, villain):
    # Things that happen when the player runs back to the field
    print_pause("You run back into the field. Luckily, \
    you don't seem to have been followed.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave. ")
    print_pause("What would you like to do?")
    choice = check_valid("(Please enter 1 or 2).")
    if choice == "1":
        house(items, villain)
    if choice == "2":
        cave(items, villain)


def house(items, villain):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print("You are about to knock when \
    the door opens and out steps a ", villain, ".")
    print_pause(" ")
    print("Eep! This is the", villain, "'s house!")
    print_pause(" ")
    print("The ", villain, " attacks you!")
    print_pause(" ")
    if "Sword of Ogoroth" in items:
        print("You pick up your Sword of Ogoroth")
    else:
        print_pause("You feel a bit under-prepared for this, \
        what with only having a tiny dagger.")
    choice = check_valid("Would you like to (1) fight or (2) run away?")
    if choice == "1":
        fight(items, villain)
    elif choice == "2":
        field(items, villain)


def play_again():
    # check if the player would like to play again
    choice = input("Would you like to play again? (y/n)")
    if choice == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif choice == "n":
        return
    else:
        play_again()


def choosing_field(items, villain):
    # playing choice at the field
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave. ")
    print_pause("What would you like to do?")
    choice = check_valid("(Please enter 1 or 2).")
    if choice == "1":
        house(items, villain)
    elif choice == "2":
        cave(items, villain)


def play_game():
    items = []
    villain = random.choice(["pirate", "gorgon", "wicked fairie"])
    intro(villain)
    choosing_field(items, villain)

play_game()
