"""
File: hangman.py
Name: Danny
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
    This program randomly selected a word from our word bank, and you could have
    designated turns (could be modified) to guess the answers. You could guess
    the word by entering 1 alphabet at a time. Guesses other than single alphabet
    were illegal format (but will not count as guess attempts). If the guess was
    correct, the program would show current result of your guess and you could continue
    your guess attempt. If was guess is wrong, available guess attempts would decrease 1.
    If you guessed correctly, the program would show the word and the program ended.
    The program also ended if you used all attempts available.
    """
    word = random_word()
    attempt_left = N_TURNS
    ans = intro(word, attempt_left)
    while attempt_left != 0:
        hangman_figure(attempt_left)
        ans, attempt_left = hangman(word, ans, attempt_left)
        if ans == word:  # if players had guess the word correctly
            print('You are correct!')
            print('You win!!')
            print('The word was: ' + word)
            break
        else:
            print('The word looks like: ' + ans)
    if attempt_left == 0:  # players failed to guess the word correctly
        hangman_figure(attempt_left)
        print('You are completely hung : (')


def hangman(word, ans, attempt_left):
    """
    :param word: str, the word randomly selected from our word bank.
    :param ans: str, the result's of player's guess, before guessing
    :param attempt_left: int, the guessing attempts left for players, before guessing
    :return ans: str, the result's of player's guess, after guessing
    :return attempt_left: int, the guessing attempts left for players, after guessing
    """
    while True:
        guess = input('Your guess: ')
        if guess.isalpha():  # make sure the input was corrected format
            if len(guess) == 1:
                guess = guess.upper()
                break
            else:
                print('illegal format.')
        else:
            print('illegal format.')
    wrong_alpha = 0  # in order to evaluate whether the player's guess was wrong
    for i in range(len(word)):
        if guess == word[i]:
            new_ans = ''
            for j in range(len(word)):
                if word[j] == guess:
                    new_ans += guess
                else:
                    new_ans += ans[j]
            ans = new_ans
        else:
            wrong_alpha += 1  # in order to evaluate whether the player's guess was wrong
    if wrong_alpha == len(word):  # if ==, the player's guess was wrong
        attempt_left -= 1
        print('There is no ' + guess + '\'s in the word.')
        print('You have ' + str(attempt_left) + ' guesses left.')
    return ans, attempt_left


def intro(word, attempt_left):
    """
    :param word: str, the word randomly selected from our word bank.
    :param attempt_left: int, the guessing attempts left for players, before guessing.
    :return: str, number of alphabets in the given words, presented in '-'
    """
    ans = ''
    for i in range(len(word)):
        ans += '-'
    print('The word looks like: ' + ans)
    print('You have ' + str(attempt_left) + ' guess left.')
    return ans


def hangman_figure(attempt_left):
    """
    This function shows the hangman figure for word guessing games with default attempts <= 11.
    The hangman figure grows as the available guessing attempts decrease.
    :param attempt_left: int, the guessing attempts left for players
    """
    if attempt_left == N_TURNS:
        print('___________')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|_____')
    if attempt_left == N_TURNS - 1:
        print('___________')
        print('|         |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|_____')
    if attempt_left == N_TURNS - 2:
        print('___________')
        print('|         |')
        print('|         O')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|_____')
    if attempt_left == N_TURNS - 3:
        print('___________')
        print('|         |')
        print('|         O')
        print('|         |')
        print('|         |')
        print('|')
        print('|')
        print('|')
        print('|_____')
    if attempt_left == N_TURNS - 4:
        print('___________')
        print('|         |')
        print('|         O')
        print('|       \\_|')
        print('|         |')
        print('|')
        print('|')
        print('|')
        print('|_____')
    if attempt_left == N_TURNS - 5:
        print('___________')
        print('|         |')
        print('|         O')
        print('|       \\_|_/')
        print('|         |')
        print('|')
        print('|')
        print('|')
        print('|_____')
    if attempt_left == N_TURNS - 6:
        print('___________')
        print('|         |')
        print('|         O')
        print('|       \\_|_/')
        print('|         |')
        print('|        /')
        print('|       |')
        print('|')
        print('|_____')
    if attempt_left == N_TURNS - 7:
        print('___________')
        print('|         |')
        print('|         O')
        print('|       \\_|_/')
        print('|         |')
        print('|        / \\')
        print('|       |   |')
        print('|')
        print('|_____')
    if attempt_left == N_TURNS - 8:
        print('___________')
        print('|         |')
        print('|         O')
        print('|       \\_|_/')
        print('|         |')
        print('|        / \\')
        print('|       |   |')
        print('|       |')
        print('|_____')
    if attempt_left == N_TURNS - 9:
        print('___________')
        print('|         |')
        print('|         O')
        print('|       \\_|_/')
        print('|         |')
        print('|        / \\')
        print('|       |   |')
        print('|       |   |')
        print('|_____')
    if attempt_left == N_TURNS - 10:
        print('___________')
        print('|         |')
        print('|        -O')
        print('|       \\_|_/')
        print('|         |')
        print('|        / \\')
        print('|       |   |')
        print('|       |   |')
        print('|_____')
    if attempt_left == N_TURNS - 11:
        print('___________')
        print('|         |')
        print('|        -O-')
        print('|       \\_|_/')
        print('|         |')
        print('|        / \\')
        print('|       |   |')
        print('|       |   |')
        print('|_____')


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
