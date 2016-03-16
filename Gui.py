from tkinter import *
import random as ra
import time


class Gui(Frame):
    # calls all the methods when the program starts
    def __init__(self):
        Frame.__init__(self, bg="#303030")  # set window background color
        self.window()
        self.chars = "r", "b", "g", "y"
        self.user_input = []
        self.com_list = []
        self.count = 0
        self.show_com_list
        self.get_next_color()
        self.red_btn()
        self.green_btn()
        self.blue_btn()
        self.yellow_btn()
        self.grid()

    def window(self):    # creates the window
        root.title("Color Blast")
        root.geometry("950x840")
        root.config(bg="#303030")

    def red_btn(self):    # creates the red button
        red = Button(self, bg="red", command=self.count_red)
        red.config(width=50, height=20)
        red["text"] = "Red"
        red.grid(row=0, column=0, padx=70, pady=70)    # sets location and space between buttons

    def blue_btn(self):    # creates the blue button
        blue = Button(self, bg="blue", command=self.count_blue)
        blue.config(width=50, height=20)
        blue["text"] = "Blue"
        blue.grid(row=0, column=2)

    def green_btn(self):    # creates the green button
        green = Button(self, bg="green", command=self.count_green)
        green.config(width=50, height=20)
        green["text"] = "Green"
        green.grid(row=2, column=0)

    def yellow_btn(self):    # creates the yellow button
        yellow = Button(self, bg="yellow", command=self.count_yellow)
        yellow.config(width=50, height=20)
        yellow["text"] = "Yellow"
        yellow.grid(row=2, column=2)

    def count_red(self):
        r = self.user_input.append("r")
        return r

    def count_blue(self):
        b = self.user_input.append("b")
        return b

    def count_green(self):
        g = self.user_input.append("g")
        return g

    def count_yellow(self):
        y = self.user_input.append("y")
        print(self.user_input)
        print(self.com_list)
        return y

    def get_next_color(self):
        if self.yellow_btn() == "y":
            b = self.com_list.append(ra.choice(self.chars))
            return b
        elif self.green_btn() == True:
            b = self.com_list.append(ra.choice(self.chars))
            return b
        elif self.blue_btn() == True:
            b = self.com_list.append(ra.choice(self.chars))
            return b
        elif self.red_btn() == True:
            b = self.com_list.append(ra.choice(self.chars))
            return b

    def show_com_list(self):
        if self.get_next_color() == "y":
            self.yellow_btn.config(bg="white")
            root.update()
            time.sleep(0.5)
            self.yellow_btn.config(bg="yellow")
            root.update()
        elif self.get_next_color() == "g":
            self.green_btn.config(bg="white")
            root.update()
            time.sleep(0.5)
            self.green_btn.config(bg="green")
            root.update()
        elif self.get_next_color() == "b":
            self.blue_btn.config(bg="white")
            root.update()
            time.sleep(.5)
            self.blue_btn.config(bg="blue")
            root.update()
        elif self.get_next_color() == "r":
            self.red_btn.config(bg="white")
            root.update()
            time.sleep(.5)
            self.red_btn.config(bg="red")
            root.update()

root = Tk()
app = Gui()
app.mainloop()