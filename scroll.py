#!/usr/bin/python

from font import Font
import random
import sys, threading, time


DEFAULT_FONT='jumper-thumb.font'    # kinda the only font, but hey maybe later i'll do wingdings or something
MARQUEE_SIZE=[5,59]                 # because that's the jumper 5 pixels high and 59 wide
KEMING=1                            # space between letters

RANDOM_TEXT=['all your base are belong to us', 'no ragrets', 'is thing on?', '1.21 gigawatts? 1.21 GIGAWATTS!? Great Scott!']
ROLL_DELAY = 0.125                  # wait this many seconds to scroll the text

DEBUGGING = 1                       # verbose things, for bedugging. Bigger numbers means more verbosity
CONSOLE_OUTPUT = True               # output scroll text to console

class Scroll:

    self.marquee_size = MARQUEE_SIZE
    self.keming_characters = 0          # number of blank spaces to append to the text
    self.font_width = 3                 # pixel width of characters in the font
    self.font_height = 5                # pixel height of characters in the font
    self.keming = KEMING                # pixel space between letters

    def __init__(self):
        self.marquee_size = MARQUEE_SIZE
        self.font = self.set_font(DEFAULT_FONT)
        self.text = self.set_text(Scroll.get_random_text())
        print(self.text)

    def set_text(self, new_text):
        if new_text == None: new_text = get_random_text()
        self.text = new_text
        return self.text

    # this one has to be in the form: [ character, [row bitmap], [column bit map] ]
    def set_font(self, font_file):
        f = Font()
        font = f.load_font(font_file)
        
        return font

    # rotate the text, with a delay, ie: scrolls the text to the right at a set speed
    def roll_text(self):
        new_text = self.text[1:] + self.text[0]
        self.text = new_text
        time.sleep(ROLL_DELAY)
        self.roll_text()
        
    def marquee_to_console(self):
        if DEBUGGING: print(self.text)
        if CONSOLE_OUTPUT:
            noop = True

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
