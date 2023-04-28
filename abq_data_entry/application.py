# abq_data_entry/application.py
''' Docstring '''

# IMPORTS ------------------------------------------------

import tkinter as tk  
from tkinter import ttk 
from . import views as v
from . import models as m
from datetime import datetime

# VARIABLES ----------------------------------------------

# CLASSES ------------------------------------------------

class Application(tk.Tk):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.model = m.CSVModel()

        self.title("ABQ Data Entry Application")
        self.columnconfigure(0, weight=1)

        ttk.Label(self,text="ABQ Data Entry Application",font=("TkDefaultFont", 16)).grid(row=0)


        self.recordform = v.DataRecordForm(self, self.model)
        self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))
        self.recordform.bind('<<SaveRecord>>', self._on_save)

        # status bar
        self.status = tk.StringVar()
        ttk.Label(self, textvariable=self.status).grid(sticky=(tk.W + tk.E), row=3, padx=10)

        self._records_saved = 0

    def _on_save(self):
        """Handles save button clicks"""
        errors = self.recordform.get_errors()
        if errors:
            self.status.set("Cannot save, error in fields: {}".format(', '.join(errors.keys())))
            return

        data = self.recordform.get()
        self.model.save_record(data)
        self._records_saved += 1
        self.status.set(
            f"{self._records_saved} records saved this session"
        )
        self.recordform.reset()


# MAIN LOOP ----------------------------------------------

def main():

    pass

    return

if __name__ == '__main__':
    main()