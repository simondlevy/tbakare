"""
File: numberguessgui.py
"""

from breezypythongui import EasyFrame
import tkinter

class NumberGuessGUI(EasyFrame):

    def __init__(self, game):

        # Instance variable to track the game.
        self.game = game

        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = f"Guessing in Range {self.game.low} - {self.game.high}")


        self.label = self.addLabel(text = f"My guess is {self.game} in {self.game.tries} guess(es)",
                                   row = 0, column = 0,
                                   sticky = "NSEW",
                                   columnspan = 3)

        # Three command buttons.
        self.addButton(text = "Too low",
                       row = 1, column = 0,
                       command = self.tooLow)

        self.addButton(text = "Too high",
                       row = 1, column = 1,
                       command = self.tooHigh)

        self.addButton(text = "Correct",
                       row = 1, column = 2,
                       command = self.correct)


    # Methods to handle user events.
    def tooLow(self):
        self.game.adjust("low")
        self.label["text"] = f"My guess is {self.game} in {self.game.tries} guess(es)"

    def tooHigh(self):
        self.game.adjust("high")
        self.label["text"] = f"My guess is {self.game} in {self.game.tries} guess(es)"

    def correct(self):
        self.game.adjust("correct")
        self.label["text"] = "I did it, Yay!"
        tkinter.messagebox.showinfo("Game Over!", f"My guess of {self.game} was correct in {self.game.tries} guess(es)")


