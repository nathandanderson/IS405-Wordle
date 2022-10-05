# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
Group 13 - Matt Perry, Jessica Kinghorn, Joseph Espiritu, Jialing Lu, Nathan Anderson
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, WordleGWindow, N_COLS, N_ROWS

def wordle():

# CHOOSE THE WORDLE WORD
    wordleWord = FIVE_LETTER_WORDS[random.randint(0,len(FIVE_LETTER_WORDS)-1)]
    wordleWordList = list(wordleWord)
    print(wordleWord)


    def enter_action(s):
        # initialize column counter, the word variable, and the word list.
        x = 0
        enteredWordList = list()
        enteredWord = ''

        # Loop through the inputted characters and construct a list based off of them
        while x <= (N_COLS-1):
            current_letter = gw.get_square_letter(gw.get_current_row(),x)
            enteredWordList.append(current_letter.lower())

            # Compare positions in entered list with wordle list to see if letters are in the correct position then color green
            if current_letter.lower() == wordleWordList[x]:
                gw.set_square_color(gw.get_current_row(),x,CORRECT_COLOR)
                gw.set_key_color(current_letter, CORRECT_COLOR)
            # Increment the column position.
            x=x+1
        # Form a word based on the inputed word list for searching through the dictionary
        for z in enteredWordList:
            enteredWord += z

        # Search through the dictionary and confirm that the word entered is in the dictionary
        if enteredWord not in FIVE_LETTER_WORDS:
            gw.show_message("Please enter a valid word.")
        # Victory condition
        elif (enteredWord == wordleWord):
            gw.show_message(f"Congrats! You won in {gw.get_current_row() + 1} attempt{'s' if gw.get_current_row() > 0 else ''}.")
        # If the word is in the dictionary then move on to the next row
        else:
            # CHANGE THE ROW TO THE NEXT ROW
            if gw.get_current_row()+1 < N_ROWS:
                gw.set_current_row(gw.get_current_row()+1)

            gw.show_message("Nice word choice! Guess again!")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
