#! python3

import csv
import random

class WinnerPicker:
    INPUT_FILE = 'sheet.csv'
    OUTPUT_FILE = 'processed_sheet.csv'
    
    def __init__(self):
        self.row_count = 0

    def process_documents(self):
        try:
            with open(self.INPUT_FILE, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                with open(self.OUTPUT_FILE, 'w') as fileOut:
                    writer = csv.writer(fileOut, delimiter=',')
                    for row in reader:
                        self.row_count += int(row[1])
                        for i in range(int(row[1])):
                            writer.writerow(row)
        except FileNotFoundError:
            print('\nRemember: the name of the input file must be "sheet" and the extension ".csv" hence "sheet.csv"\n')

    def pick_winner(self, max):
        return random.randint(1, max)
    
    def print_winner_name(self, winner):
        try:
            with open(self.OUTPUT_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if reader.line_num == winner:
                        print(row[0], row[1])
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print('\n')
    
    wp = WinnerPicker()
    wp.process_documents()
    if wp.row_count != 0:
        print(f'row count: {wp.row_count}')
        w = wp.pick_winner(wp.row_count)
        print(f'winner row: {w}')
        wp.print_winner_name(w)
    else:
        print('Failed attempt to find a winner.')
    
    print('\n')
    