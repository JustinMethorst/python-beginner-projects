from multiprocessing.resource_sharer import stop
import random

attempt_list = []

def show_score():
    if len(attempt_list) <= 0:
        print("There is currently no highscore, it's yours for the taking!")
    else:
        print("The current highscore is {} attempts".format(min(attempt_list)))

def play_again():
    play_again = input("Would you like to play again? (Enter Yes/No) ")
    attempts = 0
    show_score()
    random_number = int(random.randint(1,10))
    if play_again.lower() == "no":
        print("That's cool, have a good one!")
        wanna_play = "no"
        exit()
        

def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {} would you like to play the guessing game? (Enter Yes/No)".format(player_name))

    attempts = 0
    show_score()

    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range (between 1 and 10)")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempt_list.append(attempts)
                print("It took you {} attempts.".format(attempts))
                attempts = 0
                play_again()
                
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    
if __name__ == '__main__':
    start_game()