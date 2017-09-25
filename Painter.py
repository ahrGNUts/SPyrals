import pyautogui
from time import sleep
from random import randint


class Painter:
    def __init__(self, w, h, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        # colors, row 1
        self.BLACK = [764, 60]
        self.GREY = [788, 60]
        self.BROWN = [807, 60]
        self.RED = [830, 60]
        self.ORANGE = [851, 60]
        self.YELLOW = [871, 60]
        self.GREEN = [891, 60]
        self.LIGHT_BLUE = [915, 60]
        self.NAVY = [940, 60]
        self.PURPLE = [962, 60]
        # colors, row 2
        self.WHITE = [764, 84]
        self.LIGHT_GREY = [788, 84]
        self.LIGHT_BROWN = [807, 84]
        self.PINK = [830, 84]
        self.LIGHT_ORANGE = [851, 84]
        self.LIGHT_YELLOW = [871, 84]
        self.LIGHT_GREEN = [891, 84]
        self.PASTEL_BLUE = [915, 84]
        self.BLUE_GREY = [940, 84]
        self.LIGHT_PURPLE = [962, 84]
        # colors, row 3
        # generalize these since they can vary

        # list of all colors above
        self.COLS = [
            self.BLACK, self.GREY, self.BROWN, self.RED, self.ORANGE, self.YELLOW, self.GREEN, self.LIGHT_BLUE,
            self.NAVY, self.PURPLE, self.WHITE, self.LIGHT_GREY, self.LIGHT_BROWN, self.PINK, self.LIGHT_ORANGE,
            self.LIGHT_YELLOW, self.LIGHT_GREEN, self.LIGHT_BLUE, self.PASTEL_BLUE, self.BLUE_GREY, self.LIGHT_PURPLE
                    ]

        # width, height of canvas
        self.WIDTH = w
        self.HEIGHT = h

        # top left corner of canvas
        self.TL_X = top_left_x
        self.TL_Y = top_left_y

        # bottom right corner of canvas
        self.BR_X = bottom_right_x
        self.BR_Y = bottom_right_y
