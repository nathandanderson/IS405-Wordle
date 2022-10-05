# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
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
        x = 0
        enteredWordList = list()
        enteredWord = ''
        while x <= (N_COLS-1):
            enteredWordList.append(gw.get_square_letter(gw.get_current_row(),x).lower())
            if gw.get_square_letter(gw.get_current_row(),x).lower() == wordleWordList[x]:
                gw.set_square_color(gw.get_current_row(),x,CORRECT_COLOR)
            x=x+1
        for z in enteredWordList:
            enteredWord += z
        if enteredWord not in FIVE_LETTER_WORDS:
            gw.show_message("Please enter a valid word.")
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
