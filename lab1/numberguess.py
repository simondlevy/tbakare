"""
Author: Toluwalope Bakare
Project 1
File: numberguess.py 

"""

import random
import math

class NumberGuess():

    def __init__(self,low=1,high=100):
        self.low = low
        self.high = high
        self.tries = 1

    def guess(self):
        ans = (self.low + self.high)//2
        return ans

    def adjust(self, word):

        match word:
            case "low":
                self.low = self.guess()
                self.tries += 1
                return self.guess()
            case "high":
                self.high = self.guess()
                self.tries += 1
                return self.guess()
            case _:
                pass

    def __str__(self):                          
        """Returns the string representation of the counter."""
        return str(self.guess())
