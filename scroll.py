#!/usr/bin/python

import sched, time
import font

JUMPER_THUMB = 1

class Scroll:

    font = JUMPER_THUMB
    marquee_size = [0,0]
    text = ''

    def __init__(self):
        self.marquee_size = [0,0]
        self.font = JUMPER_THUMB
        self.text = ''


    def set_text(new_text):
        self.text = new_text

    # this one has to be in the form: [ character, [row bitmap], [column bit map] ]
    def set_font(self, font_file):
        font = Font.load_font(font_file)
        
        return font

    def roll_text():
        return


if __name__ == '__main__':
    this = Scroll()
    this.set_font('jumper_thumb.font')
    




