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
import pickle

def loadfont(infile):
    with open(infile, 'r') as f:
        character_dict = dict()
        for line in f:
            if len(line) < 2: break
            row = []
            key = None
            tuple = line.rstrip().split(',')
            for element in tuple:
                if (tuple.index(element) == 0 and key == None):
                    key = chr(int(element))
                else:
                    this_row = []
                    for col_counter in range(len(element)):
                            this_bit = True if element[col_counter] == '1' else False
                            this_row.append(this_bit)
                    row.append(this_row)
            character_dict[key] = [row,list(zip(*row))]
    return character_dict

def savefont(character_dict, outfile):
    pickle.dump(character_dict, open(outfile, 'wb'))
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="infile")
    parser.add_argument("-o", "--outfile", help="outfile")
    args = parser.parse_args()

    if not (args.infile and args.outfile):
        raise ValueError("missing parameters, use -h for help")

    savefont(loadfont(args.infile), args.outfile)



