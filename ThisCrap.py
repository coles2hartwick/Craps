# Sam Cole
# Craps is the game you are going to play
# going to be asked for a bankroll or the amount of money the user has and then play the game
import random as rand
import sys


def create():
    bankroll = int(input("What is your bankroll?"))
    return bankroll


def roll_dice():
    roll = rand.randint(1, 6)
    roll2 = rand.randint(1, 6)
    return roll + roll2


def play_game():
    print("Press enter to play craps")
    input()
    bankroll = create()
    while bankroll > 0:
        print("Place your bet")
        bet = int(input())
        while 0 < bet <= bankroll:
            bankroll = bankroll - bet
            roll = roll_dice()
            if roll == 7 or roll == 11:
                print(f"Congratulations you rolled a {roll} you win")
                bet = bet * 2
                bankroll = bet + bankroll
            elif roll == 2 or roll == 3 or roll == 12:
                print(f"Sorry we you rolled a {roll} you lost")
                print(f"You lost {bet} dollars")
            else:
                print(f"You rolled a {roll} you need to roll that to win if you roll a 7 you will lose")
                print("press enter to roll again")
                input()
                roll2 = 0
                while roll2 != roll and roll2 != 7:
                    roll2 = roll_dice()
                    print(roll2)
                if roll2 == roll:
                    print(f"Congratulations you won by rolling a {roll} again!")
                    bet = bet * 2
                    bankroll = bet + bankroll
                else:
                    print("Sorry you lost, you rolled a 7")


play_game()
