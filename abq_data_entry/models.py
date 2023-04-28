# abq_data_entry/models.py
''' Docstring '''

# IMPORTS ------------------------------------------------

import csv
from pathlib import Path
from datetime import datetime
import os

from .constants import FieldTypes as FT

# VARIABLES ----------------------------------------------

# CLASSES ------------------------------------------------

class CSVModel:
    ''' CSV file storage '''
    
    fields = {
        "Date": {'req': True, 'type': FT.iso_date_string},
        "Time": {'req': True, 'type': FT.string_list, 'values': ['8:00', '12:00', '16:00', '20:00']},
        "Technician": {'req': True, 'type':  FT.string},
        "Lab": {'req': True, 'type': FT.short_string_list,'values': ['A', 'B', 'C']},
        "Plot": {'req': True, 'type': FT.string_list,'values': [str(x) for x in range(1, 21)]},
        "Seed Sample":  {'req': True, 'type': FT.string},
        "Humidity": {'req': True, 'type': FT.decimal,'min': 0.5, 'max': 52.0, 'inc': .01},
        "Light": {'req': True, 'type': FT.decimal,'min': 0, 'max': 100.0, 'inc': .01},
        "Temperature": {'req': True, 'type': FT.decimal,'min': 4, 'max': 40, 'inc': .01},
        "Equipment Fault": {'req': False, 'type': FT.boolean},
        "Plants": {'req': True, 'type': FT.integer, 'min': 0, 'max': 20},
        "Blossoms": {'req': True, 'type': FT.integer, 'min': 0, 'max': 1000},
        "Fruit": {'req': True, 'type': FT.integer, 'min': 0, 'max': 1000},
        "Min Height": {'req': True, 'type': FT.decimal,'min': 0, 'max': 1000, 'inc': .01},
        "Max Height": {'req': True, 'type': FT.decimal,'min': 0, 'max': 1000, 'inc': .01},
        "Med Height": {'req': True, 'type': FT.decimal,'min': 0, 'max': 1000, 'inc': .01},
        "Notes": {'req': False, 'type': FT.string}
    }

    def __init__(self):
        
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = "abq_data_record_{}.csv".format(datestring)
        self.file = Path(filename)
        
        file_exists = os.access(self.file, os.F_OK)
        parent_writeable = os.access(self.file.parent, os.W_OK)
        file_writeable = os.access(self.file, os.W_OK)

        if (
            (not file_exists and not parent_writeable) or
            (file_exists and not file_writeable)
        ):
            msg = f'Permission denied while accessing file: {filename}'
            raise PermissionError(msg)
        
    def save_record(self,data):
        '''Save a dict of data to the CSV file'''
        new_file_check = not self.file.exists()
        
        with open(self.file, 'a', newline='') as file_output:
            csvwriter = csv.DictWriter(file_output, fieldnames=self.fields.keys())
            if new_file_check:
                csvwriter.writeheader()
            csvwriter.writerow(data)


# MAIN LOOP ----------------------------------------------

def main():

    pass

    return

if __name__ == '__main__':
    main()

