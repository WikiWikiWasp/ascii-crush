########################################
# ASCII CRUSH
# Author: Jason Flinn
# Date: September 11th 2018
########################################

import sys

def title():
    print('='*30)
    print('-'*7 + ' ASCII  CRUSH ' + '-'*7)
    print('='*30)
    print()


# TODO: pythonic formating
def menu():

    cflag = True
    while cflag:
        print('1. Play\n2. Help\n3. Quit\n')
        choice = input('> ')
        if choice == 1:
            print('Please choose difficulty:')
            print('1. Easy\n2. Medium\n3. Hard\n')
            choice = input('> ')
            cflag = False
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