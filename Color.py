import random as ra
import time


class Color:
    point = 0

    def __init__(self):
        print("hello")

    def random_pattern(self):
        rand = ra.randint(4)
        return rand

    def user_input(self):
        global point
        if self.user_input() == self.random_pattern():
            point += 1
            return point

