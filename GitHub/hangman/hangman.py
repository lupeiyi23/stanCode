"""
File: hangman.py
Name: Luna
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is a hangman game. Players have N_TURNS opportunities for wrong guesses.
    The characters of the word will not be revealed if players do not make correct guesses.
    Only 1 character is allowed to guess for each round.
    """
    word = random_word()
    dashed = ''
    guesses_left = N_TURNS
    for i in range(len(word)):
        dashed += '-'
    while True:
        # players win
        if word == dashed:
            break
        # players lose the game while no guesses left
        elif guesses_left == 0:
            break
        else:
            print('The word looks like '+str(dashed))
            print('You have '+str(guesses_left)+' wrong guesses left.')
            while True:
                guess = input('Your guess: ')
                # check the format of inputs: should be 1 character of alphabet
                if not guess.isalpha():
                    print('illegal format.')
                elif len(guess) != 1:
                    print('illegal format.')
                else:
                    break
            # case-insensitive
            if guess.islower():
                guess = guess.upper()
            # when players make a correct guess: all correct characters in the word will be revealed from dashed
            if word.find(guess) != -1:
                ans = ''
                for j in range(len(word)):
                    if word[j] == guess:
                        ans += guess
                    else:
                        ans += dashed[j]
                dashed = ans
                print('You are correct!')
            # when players make an incorrect guess: players lose 1 chance
            else:
                print("There is no "+str(guess)+"'s in the word.")
                guesses_left -= 1
    if word == dashed:
        print('You win!!')
    else:
        print('You are completely hung :(')
    print('The word was: ' + str(word))


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
