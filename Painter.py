import pyautogui
from time import sleep
from random import randint


class Painter:
    def __init__(self, w, h, top_left_x, top_left_y, bottom_right_x, bottom_right_y, distance):
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
        self.ALL_COLORS = [
            self.BLACK, self.GREY, self.BROWN, self.RED, self.ORANGE, self.YELLOW, self.GREEN, self.LIGHT_BLUE,
            self.NAVY, self.PURPLE, self.WHITE, self.LIGHT_GREY, self.LIGHT_BROWN, self.PINK, self.LIGHT_ORANGE,
            self.LIGHT_YELLOW, self.LIGHT_GREEN, self.LIGHT_BLUE, self.PASTEL_BLUE, self.BLUE_GREY, self.LIGHT_PURPLE
                    ]

        # color coordinates for single and dual color spirals
        self.cols = []

        # width, height of canvas
        self.WIDTH = w
        self.HEIGHT = h

        # top left corner of canvas
        self.TL_X = top_left_x
        self.TL_Y = top_left_y

        # bottom right corner of canvas
        self.BR_X = bottom_right_x
        self.BR_Y = bottom_right_y

        # initial spiral distance
        self.distance = distance

    # click a different color from the list of colors
    def changeColor(self):
        idx = randint(0, len(self.ALL_COLORS)-1)
        pyautogui.click(self.ALL_COLORS[idx][0], self.ALL_COLORS[idx][1])

    # draws a square spiral. numSpirals dictates the number of spirals to draw. if numSpirals is 0, it will draw spirals
    # infinitely until interrupted. otherwise it will draw the number of spirals passed to drawMode. if numSpirals is
    # not numeric, it will draw one spiral and stop.
    # drawType will dictate if the spiral wil be one color, two colors, or potentially all the colors in the COLS list
    # for drawType, 1 = 1 color, 2 = 2 colors, everything else will be full color range
    def drawSquareSpiral(self, numSpirals, drawType):

       
