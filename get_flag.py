"""
Opens a popup window to ask for user input and returns it.
Todo: cleanup, refactor, validate input
"""

import tkinter as tk
from tkinter import simpledialog


def get_flag():
    """
    Opens a popup window to ask for user input and returns it.
    :return: user input
    :rtype:
    """
    root = tk.Tk()
    root.withdraw()
    flag = simpledialog.askstring(title="Flag",
                                  prompt="Flag?:")
    return flag
