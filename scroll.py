#!/usr/bin/python

import sched, time
from threading import *
from font import Font
import random



DEFAULT_FONT='jumper-thumb.font'    # kinda the only font, but hey maybe later i'll do wingdings or something
MARQUEE_SIZE=(3,59)                 # because that's the jumper 5 pixels high and 59 wide
KEMING=1                            # space between letters

RANDOM_TEXT=['ipsum lorem', 'all your base are belong to us', 'no ragrets', 'is thing on?', '1.21 gigawatts? 1.21 GIGAWATTS!? Great Scott!']

DEBUGGING = True                    # verbose things, for bedugging

class Scroll:

    marquee_size = (0,0)
    marquee_text_size = MARQUEE_SIZE
    text = ''

    def __init__(self):
        self.marquee_size = MARQUEE_SIZE
        self.font = self.set_font(DEFAULT_FONT)
        self.text = Scroll.get_random_text()


    def set_text(self, new_text):
        if new_text == None: new_text = get_random_text()
        self.text = new_text

    # this one has to be in the form: [ character, [row bitmap], [column bit map] ]
    def set_font(self, font_file):
        f = Font()
        self.font = f.load_font(font_file)

    def roll_text(self):
        new_text = self.text[1:] + self.text[0]
        self.text = new_text
        # output to console
        
        if DEBUGGING: marquee_to_console()

    def output_text(self):
        while(True):
            marquee_to_console()
            time.sleep(1)


    def marquee_to_console(self):
        print(self.text)

    def get_random_text ():
        return random.choice(RANDOM_TEXT)

if __name__ == '__main__':
    scroller = Scroll()
    



