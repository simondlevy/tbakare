"""
Author: Toluwalope Bakare
Project 1
File: layoutdemo.py 

"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class LayoutDemo(EasyFrame):
    """Displays labels in the window's quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0,
                      sticky = "NSEW",
                      foreground = "red",
                      font = Font(size = 24, weight = "bold"))
        self.addLabel(text = "(0, 1)", row = 0, column = 1,
                      sticky = "NSEW",
                      foreground = "red",
                      font = Font(size = 24, weight = "bold"))
        self.addLabel(text = "(1, 0)", row = 1, column = 0,
                      sticky = "NSEW",
                      foreground = "red",
                      font = Font(size = 24, weight = "bold"))
        self.addLabel(text = "(1, 1)", row = 1, column = 1,
                      sticky = "NSEW",
                      foreground = "red",
                      font = Font(size = 24, weight = "bold"))

def main():
    """The starting point for launching the program."""
    LayoutDemo().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
