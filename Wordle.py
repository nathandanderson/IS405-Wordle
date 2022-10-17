# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
Group 13 - Matt Perry, Jessica Kinghorn, Joseph Espiritu, Jialing Lu, Nathan Anderson
"""

from ast import And
from dataclasses import MISSING
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, WordleGWindow, N_COLS, N_ROWS

def wordle():

# CHOOSE THE WORDLE WORD
    wordleWord = FIVE_LETTER_WORDS[random.randint(0,len(FIVE_LETTER_WORDS) - 1)]
    wordleWordList = list(wordleWord)
    print(wordleWord)


    def enter_action(s):
        # initialize column counter, the word variable, and the word list.
        enteredWordList = list()

        # Loop through the inputted characters and construct a list based off of them
        for i in range(N_COLS) :
            current_letter = gw.get_square_letter(gw.get_current_row(), i).lower()
            enteredWordList.append(current_letter.lower())

        # Form a word based on the inputed word list for searching through the dictionary
        enteredWord = ''.join(enteredWordList)

        print(enteredWord)
        if enteredWord not in FIVE_LETTER_WORDS:
            gw.show_message("Please enter a valid word.")
            gw.set_current_row(gw.get_current_row())
            return

        # THIS DOES THE COLORS FOR THE WORDLE BY LOOPING THROUGH A SERIES OF IF STATEMENTS TO ASSIGN THE CORRECT COLOR. 
        letterUsed = []
        correctLetters = []

        print(wordleWordList)
        print(enteredWordList)
        for i in range(N_COLS) :
            current_letter = gw.get_square_letter(gw.get_current_row(), i).lower()
            print(current_letter)
            if current_letter == wordleWordList[i] :
                gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                gw.set_key_color(current_letter.upper(), CORRECT_COLOR)
                letterUsed.append(current_letter)
                correctLetters.append(current_letter)
                print('Green' + str(letterUsed))

        for i in range(N_COLS) :
            current_letter = gw.get_square_letter(gw.get_current_row(), i).lower()
            if (current_letter != wordleWordList[i]) :
                if current_letter in wordleWordList :
                    letterUsed.append(current_letter)
                    print(wordleWordList.count(current_letter), letterUsed.count(current_letter))
                    print('Yellows' + str(letterUsed))
                    if (wordleWordList.count(current_letter) >= letterUsed.count(current_letter)) :
                        gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                        if (current_letter not in correctLetters) :
                            gw.set_key_color(current_letter.upper(), PRESENT_COLOR)
                    else :
                        gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                        if (current_letter not in correctLetters) :
                            gw.set_key_color(current_letter.upper(), MISSING_COLOR)
                else :
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                    if (current_letter not in correctLetters) :
                        gw.set_key_color(current_letter.upper(), MISSING_COLOR)

        # Victory condition
        if (enteredWord == wordleWord):
            gw.show_message(f"Congrats! You won in {gw.get_current_row() + 1} attempt{'s' if gw.get_current_row() > 0 else ''}.")
        # Else if the word is in the dictionary then move on to the next row
        else:
            if gw.get_current_row() < N_ROWS - 1:
                gw.set_current_row(gw.get_current_row() + 1)
                gw.show_message("Nice word choice! Guess again!")
            else :
                gw.show_message(f"Sorry! The correct word was {wordleWord}.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
