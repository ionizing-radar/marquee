#!/usr/bin/python

from font import Font
import random
import sys, threading, time


DEFAULT_FONT='jumper-thumb.font'    # kinda the only font, but hey maybe later i'll do wingdings or something
MARQUEE_SIZE=[5,59]                 # because that's the jumper 5 pixels high and 59 wide
KEMING=1                            # space between letters

RANDOM_TEXT=['ipsum lorem', 'all your base are belong to us', 'no ragrets', 'is thing on?', '1.21 gigawatts? 1.21 GIGAWATTS!? Great Scott!']
ROLL_DELAY = 0.125                  # wait this many seconds to scroll the text

DEBUGGING = True                    # verbose things, for bedugging

class Scroll:


    def __init__(self):
        self.marquee_size = MARQUEE_SIZE
        self.font = self.set_font(DEFAULT_FONT)
        self.text = self.set_text(Scroll.get_random_text())


    def set_text(self, new_text):
        if new_text == None: new_text = get_random_text()
        self.text = new_text
        print(self.font)
        sys.exit()

    # this one has to be in the form: [ character, [row bitmap], [column bit map] ]
    def set_font(self, font_file):
        f = Font()
        return f.load_font(font_file)

    def roll_text(self):
        new_text = self.text[1:] + self.text[0]
        self.text = new_text
        time.sleep(ROLL_DELAY)
        self.roll_text()
        
    def marquee_to_console(self):
        print(self.text)
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
