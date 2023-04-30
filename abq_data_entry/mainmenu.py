# mainmenu.py
''' The menu file for the ABQ Data Entry Application.  Part of view, but large enough to be it's own module. '''

# IMPORTS ------------------------------------------------

import tkinter as tk 
from tkinter import messagebox

# VARIABLES ----------------------------------------------

# CLASSES ------------------------------------------------

class MainMenu(tk.Menu):
    '''The Application's main menu.'''

    def _event(self, sequence):
        def callback(*_):
            root = self.master.winfo_toplevel()
            root.event_generate(sequence)
        return callback

    def __init__(self, parent, settings, **kwargs):
        super().__init__(parent, **kwargs)
        self.settings = settings
        
        # File Menu --------------------------------
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(
            label="Select file...",
            command=self._event('<<FileSelect>>')
        )
        
        file_menu.add_separator()
        file_menu.add_command(
            label="Quit",
            command=self._event('<<FileQuit>>')
        )
        
        # Options Menu ----------------------
        options_menu = tk.Menu(self, tearoff=False)
        options_menu.add_checkbutton(
            label='Autofill Date',
            variable=self.settings['autofill date']
        )
        options_menu.add_checkbutton(
            label='Autofill Sheet Data',
            variable=self.settings['autofill sheet data']
        )

        # Help Menu ------
        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(
            label='About...',
            command=self.show_about
        )
        
        # Add menus in the right order...
        self.add_cascade(label='File', menu=file_menu)
        self.add_cascade(label='Options', menu=options_menu)
        self.add_cascade(label='Help', menu=help_menu)

    def show_about(self):
        '''Show the about dialog'''
        
        about_message = 'ABQ Data Entry'
        about_detail = (
            'tutorial from Alan D Moore\n'
            'followed by Vektra Casler\n'
            'For assistance, please contact the author.'
        )
        messagebox.showinfo(
            title='About',
            message=about_message,
            detail=about_detail
        )

# MAIN LOOP ----------------------------------------------

def main():

    pass

    return

if __name__ == '__main__':
    main()