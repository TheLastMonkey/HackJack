#!/usr/bin/python3
import os
import time

os.system("clear")

card_c = 0
i = 0
the_n_card = 0
hot = False

def count():
    global i
    global card_c
    global the_n_card
    global hot
    os.system("clear")
    print("Current is ",i)
    print("Neutral Cards :",the_n_card)
    print("Toatal Cards Counted : ",card_c)
    print("The Deck is Hot?:", hot)
    print("""
Press l If The Card is Low [Twos Though Sixs] and Up The Count
Press h If The Card is High [Tens Though Aces] and Lower The Count
Press n If The Card is Neutral [Seven, Eights, and Nines] to Keep The Count Neutral
Press r to Reset All
Press q to Quit
    """)
    ccount = input ("Input A Action : ")
    if ccount == "l":
        i=i+1
        card_c = card_c + 1
        if i >= 4:
            hot = True
        print("The New Count is:",i)
        time.sleep(0.5)
        count()
    elif ccount == "h":
        i=i-1
        if i <= 3:
            hot = False
        card_c = card_c + 1
        print("The New Count is:", i)
        time.sleep(0.5)
        count()
    elif ccount == "n":
        card_c = card_c + 1
        the_n_card=the_n_card+1
        print("Count Unchanged. The Count is:", i)
        time.sleep(0.5)
        count()
    elif ccount == "q":
        print("Quitting")
    elif ccount == "r":
        print("Resetting")
        i=0
        card_c = 0
        the_n_card=0
        hot = False
        time.sleep(0.5)
        count()
    else:
        print("huh?")
        time.sleep(1)
        count()
count();

