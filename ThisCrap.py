# Sam Cole
# Craps is the game you are going to play
# going to be asked for a bankroll or the amount of money the user has and then play the game
import random as rand
import sys


def create():
    bankroll = 0
    while bankroll == 0:
        bankroll = int(input("What is your bankroll?\n>"))
        if bankroll < 0:
            print("Im sorry that is not a valid bankroll please choose something over $0")
            bankroll = 0
    return bankroll


def roll_dice():
    roll = rand.randint(1, 6)
    roll2 = rand.randint(1, 6)
    return roll + roll2


def play_game():
    print("Press enter to play craps")
    input()
    bankroll = create()
    while bankroll > 0:  # makes sure that the bankroll is valid so the player can play
        print("Place your bet")
        bet = int(input(">"))
        if bet < 0 or bet > bankroll:  # makes sure that the bet is a valid number
            print("Im sorry that bet is not valid please choose something greater than 0")
            print(f"and less than or equal to {bankroll}")
        else:
            while 0 < bet <= bankroll:  # applies the bet to bankroll
                bankroll = bankroll - bet
                roll = roll_dice()
                if roll == 7 or roll == 11:  # determines the value of the roll and whether or not the person wins loses or keeps rolling
                    print(f"Congratulations you rolled a {roll} you win")
                    bet = bet * 2
                    bankroll = bet + bankroll
                    print(f"Your bankroll is now {bankroll} dollars")
                    bet = 0
                elif roll == 2 or roll == 3 or roll == 12:
                    print(f"Sorry you rolled a {roll} you lost")
                    print(f"You lost {bet} dollars")
                    print(f"Your bankroll is now {bankroll}")
                    bet = 0
                else:
                    print(f"You rolled a {roll} you need to roll that again to win or if you roll a 7 you will lose, good luck!")
                    print("press enter to roll again")
                    input()
                    roll2 = 0
                    while roll2 != roll and roll2 != 7:  # Keeps rolling to see if you win or lose
                        roll2 = roll_dice()
                        print(roll2)
                    if roll2 == roll:
                        print(f"Congratulations you won by rolling a {roll} again!")
                        bet = bet * 2
                        bankroll = bet + bankroll
                        print(f"Your bankroll is {bankroll} dollars")
                        bet = 0
                    else:
                        print("Sorry you lost, you rolled a 7")
                        print(f"You lost {bet} dollars and your bankroll is {bankroll}")
                        bet = 0
                print("Would you like to play again? Y or N")
                answer = input(">")
                if answer == "N" or answer == "n":  # checks if you would want to play again and if you don"t kicks you from the program and gives your bankroll back
                    print(f"Thanks for the game here's your'e {bankroll} dollars back have a nice day!")
                    sys.exit()
                elif bankroll == 0:
                    print("I'm sorry your bankroll is 0 you lost all your money have a good day!")
                    sys.exit()


play_game()
