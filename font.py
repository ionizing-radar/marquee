#!/usr/bin/python
# reads the font file, makes a dictionary from it
#   each line defines a character and is comma delimitted.  the first value is the ascii of the character, and the next values are a row-by-row bitmap
#   ie the letter 'a' shown in a 3x5 bitmap as:
#           -> 000
#       ##  -> 110
#        ## -> 011
#       # # -> 101
#       ### -> 111
#
#   will be encoded as: 97,000,110,011,101,111
# the resultant dictionary takes the form: [ key [list of rows], [list of columns] ]
#   an 'a' will thus look like:
#   ['a',
#   [[False, False, False], [True, True, False], [False, True, True], [True, False, True], [True, True, True]], 
#   [(False, True, False, True, True), (False, True, True, False, True), (False, False, True, True, True)]]

import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", help="infile")
parser.add_argument("-o", "--outfile", help="outfile")
args = parser.parse_args()

if not (args.infile and args.outfile):
    print("missing parameters, use -h for help")
    exit()

character_dict = dict()

with open(args.infile, 'r') as f:
    for line in f:
        if len(line) < 2: break
        row = []
        key = None
        tuple = line.rstrip().split(',')
        rows = len(tuple)-1     # have to subtract 1 because the element in the tuple is the dictionary key
        cols = len(tuple[1])    # ditto, can't use the 0th element because it's a key
        for element in tuple:
            col_char = [[False]*rows]*cols
            row_counter = 0
            if (tuple.index(element) == 0 and key == None):
                key = chr(int(element))
            else:
                this_row = []
                for col_counter in range(len(element)):
                        this_bit = True if element[col_counter] == '1' else False
                        this_row.append(this_bit)
                        col_char[row_counter][col_counter] = this_bit
                row.append(this_row)
            row_counter = row_counter + 1
        character_dict[key] = [row,list(zip(*row))]

print( character_dict['a'] )

