# python.py
''' Docstring '''

# IMPORTS ------------------------------------------------

import tkinter as tk 
from tkinter import messagebox

# VARIABLES ----------------------------------------------

# MAIN LOOP ----------------------------------------------

def main():

    see_more = messagebox.askyesno(
        title='Do you like Star Wars?',
        message="Disney Star Wars, specifically.",
        detail="Click NO to quit."
    )
    
    if not see_more:
        exit()

    messagebox.showinfo(
        title='The Mandolorian says...',
        message="This is the way.",
        detail="If only they had some details about this."
    )

    return

if __name__ == '__main__':
    main()
