"""Simulating a dice game Craps"""
import random
from tabulate import tabulate

winner = 0
loser = 0
wins = {}
losses = {}


def roll_dice():
    global die1
    global die2
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple


def display_dice(dice):
    """Display one roll of the two dice"""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f"Player rolled {die1} + {die2} = {sum(dice)}")


def play_game():
    for i in range(1, 50):  # number of rolls
        die_values = roll_dice()  # first roll
        display_dice(die_values)

    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):  # win
        game_status = "won"

    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = "lost"

    else:  # remember point
        game_status = "CONTINUE"
        my_poimt = sum_of_dice
        print("Point is", my_poimt)

    while game_status == "CONTINUE":
        die_values = roll_dice()
        display_dice(die_values)
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_poimt:  # win by making point
            game_status = "WON"

        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = "Lost"

    # Displays 'wins' or 'loses' messages
    if game_status == "WON":
        print("Player wins")
    else:
        print("Player loses")
