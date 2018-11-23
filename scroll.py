#!/usr/bin/python

from font import Font
import random
import sys, threading, time


DEFAULT_FONT='jumper-thumb.font'    # kinda the only font, but hey maybe later i'll do wingdings or something
MARQUEE_SIZE=[5,59]                 # because that's the jumper 5 pixels high and 59 wide
MARQUEE_ROWS=0                      # index for getting the number of rows in the marquee
MARQUEE_COLS=1                      # index for getting the number of cols in the marquee
KEMING=1                            # space between letters

RANDOM_TEXT=['all your base are belong to us', 'no ragrets', '1.21 gigawatts? 1.21 GIGAWATTS!? Great Scott!']
ROLL_DELAY = 0.125                  # wait this many seconds to scroll the text

DEBUGGING = 1                       # verbose things, for bedugging. Bigger numbers means more verbosity
CONSOLE_OUTPUT = True               # output scroll text to console

class Scroll:

    marquee_size = MARQUEE_SIZE
    keming_characters = 0                       # number of blank spaces to append to the text
    font_width = 3                              # pixel width of characters in the font
    font_height = 5                             # pixel height of characters in the font
    keming = KEMING                             # pixel space between letters
    keming_col = [[False]*font_height]*keming   # keming turned into spaces between letters when displayed
 

    def __init__(self):
        self.marquee_size = MARQUEE_SIZE
        self.font = self.set_font(DEFAULT_FONT)
        self.text = self.set_text(Scroll.get_random_text())
        self.keming_col = [[False]*self.font_height]*self.keming
 
        print(self.text)

    def set_text(self, new_text):
        if new_text == None: new_text = get_random_text()
        self.text = new_text
        marquee_character_width = int(self.marquee_size[MARQUEE_COLS]/self.font_width)  # how many characters fit in the marquee
        if len(self.text) > marquee_character_width:
            padding = ' '*5
        else: 
            padding = '  '
        self.text = self.text + padding
        return self.text

    # this one has to be in the form: [ character, [row bitmap], [column bit map] ]
    def set_font(self, font_file):
        # get the font
        f = Font()
        font = f.load_font(font_file)
        self.font_width = len(font['i'][Font.CHARACTER_BY_ROWS][Font.ROW])
        self.font_height = len(font['i'][Font.CHARACTER_BY_ROWS])

        return font

    # rotate the text, with a delay, ie: scrolls the text to the right at a set speed
    def roll_text(self):
        new_text = self.text[1:] + self.text[0]
        self.text = new_text
        time.sleep(ROLL_DELAY)
        self.roll_text()
        
    def marquee_to_console(self):
        if DEBUGGING > 1: print(self.text)
        display = []
        if CONSOLE_OUTPUT:
            for letter in self.text:
                if len(display) >= MARQUEE_SIZE[MARQUEE_COLS]: break
                for col in self.font[letter][MARQUEE_COLS]:
                    display = display + [col]
                display = display + self.keming_col
            while len(display) > MARQUEE_SIZE[MARQUEE_COLS]:
                del display[-1]

        for col in display:
            this_col = ''
            for bit in col:
                this_bit = chr(48) if bit else chr(32)
                this_col = this_col + this_bit
            this_col = this_col[::-1]
            print(this_col)


        time.sleep(ROLL_DELAY)
        self.marquee_to_console()


    def get_random_text ():
        return random.choice(RANDOM_TEXT)



if __name__ == '__main__':
    scroller = Scroll()
    
    scrolling_thread = threading.Thread(target=scroller.marquee_to_console)
    scrolling_thread.setDaemon(True)
    scrolling_thread.start()

    rolling_thread = threading.Thread(target=scroller.roll_text)
    rolling_thread.setDaemon(True)
    rolling_thread.start()

    while True:
        in_str = input('Press enter to quit.\n')
        print ('bye')
        sys.exit()
