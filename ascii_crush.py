########################################
# ASCII CRUSH
# Author: Jason Flinn
# Date: September 11th 2018
########################################

import sys

#terminal text colors
BLUE = '\033[0;34m'
RED = '\033[0;31m'
GREEN = '\033[;32m'
NC = '\033[0m' #no color

def title():
    print('='*30)
    print('-'*7 + ' ASCII  CRUSH ' + '-'*7)
    print('='*30)
    print()


# TODO: pythonic formating
# TODO: difficulty validation
# TODO: Help message
# TODO: determine if menu() should return a value or serve as a "main" function and call the other game's functions
def menu():

    while True:
        print('1. Play\n2. Help\n3. Quit\n')
        # input validation
        try:
            choice = int(input('> '))
        except NameError:
            print('Error. Invalid input. Enter a value between 1 - 3.\n')
            continue
        
        if not choice in range(1, 4):
            print('Error. Invalid input. Enter a value between 1 - 3.\n')
            continue

        # menu actions
        if choice == 1:
            print('Please choose difficulty:')
            print('1. Easy\n2. Medium\n3. Hard\n')
            diff = input('> ')
        elif choice == 2:
            print('<Help Message>\n')
        elif choice == 3:
            print('Quiting...\n')
            sys.exit()
        else:
            print('Please enter a valid menu choice:\n')
            choice = input('> ')


def draw_board():
    pass


def fill_board():
    pass


def match_chars():
    pass


def remove_match():
    pass


if __name__ == '__main__':
    menu()