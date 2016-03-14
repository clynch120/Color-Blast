import random as ra
import time


class Color:
    point = 0

    def __init__(self):
        print("hello")

    def random_pattern(self):
        rand = ra.randint(4)
        time.sleep(1)
        return rand

    def user_input(self):
        global point
        if self.user_input() == self.random_pattern():
            point += 1
            return point

r_list = []
user_list = []
j = 0

while user_list == r_list:
    user_list = []
    r_list.append(ra.randint(1, 4))
    print(r_list[j])
    user = input("Your turn : ")
    user_list = [int(x) for x in user.split()]
    j += 1