# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from ast import And
from dataclasses import MISSING
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, WordleGWindow, N_COLS, N_ROWS

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

        # THIS DOES THE COLORS FOR THE WORDLE BY LOOPING THROUGH A SERIES OF IF STATEMENTS TO ASSIGN THE CORRECT COLOR.
            for y in enteredWordList:
                if current_letter.lower() == wordleWordList[x]:
                    gw.set_square_color(gw.get_current_row(),x,CORRECT_COLOR)
                    gw.set_key_color(current_letter, CORRECT_COLOR)
                elif current_letter.lower() in wordleWordList:
                    gw.set_square_color(gw.get_current_row(),x,PRESENT_COLOR)
                    gw.set_key_color(current_letter, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(),x,MISSING_COLOR)
                    gw.set_key_color(current_letter, MISSING_COLOR)

            # Increment the column position.
            x=x+1

        # Form a word based on the inputed word list for searching through the dictionary
        for z in enteredWordList:
            enteredWord += z

        # Search through the dictionary and confirm that the word entered is in the dictionary
        if enteredWord not in FIVE_LETTER_WORDS:
            gw.show_message("Please enter a valid word.")

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
