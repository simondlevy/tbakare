"""
Author: Toluwalope Bakare
Project 1
File: ninecells.py 

"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class NineCells(EasyFrame):
    """Displays labels in the window's quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        for hor in range(3):
            for ver in range(3):
                self.addLabel(text = f"({hor},{ver})", row = hor, column = ver,
                      sticky = "NSEW",
                      foreground = "red",
                      font = Font(size = 24, weight = "bold"))
        
def main():
    """The starting point for launching the program."""
    NineCells().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
