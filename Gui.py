from tkinter import *
import random as ra
import time


class Gui(Frame):
    # calls all the methods when the program starts
    def __init__(self):
        Frame.__init__(self, bg="#303030")  # set window background color
        self.window()
        self.level()
        self.red_btn()
        self.green_btn()
        self.blue_btn()
        self.yellow_btn()
        self.grid()
        self.count = 0
        self.user_input = []
        self.com_list = []

    def level(self):    # creates pop up window
        top = Toplevel()
        top.attributes("-topmost", 1)
        top.title("Difficultly level")
        top.geometry("250x100")
        msg = Message(top, text="Enter Difficultly : 1 - 9", width=150)
        msg.pack()
        e = Entry(top)
        e.pack()
        button = Button(top, text="Select", command=top.destroy)
        button.pack()

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
        blue.grid(row=2, column=0)

    def green_btn(self):    # creates the green button
        green = Button(self, bg="green", command=self.count_green)
        green.config(width=50, height=20)
        green["text"] = "Green"
        green.grid(row=0, column=2)

    def yellow_btn(self):    # creates the yellow button
        yellow = Button(self, bg="yellow", command=self.count_yellow)
        yellow.config(width=50, height=20)
        yellow["text"] = "Yellow"
        yellow.grid(row=2, column=2)

    def count_red(self):
        r = self.user_input.append(1)
        return r

    def count_blue(self):
        b = self.user_input.append(2)
        return b

    def count_green(self):
        g = self.user_input.append(3)
        return g

    def count_yellow(self):
        y = self.user_input.append(4)
        print(self.user_input)
        return y

    def computer_list(self):
        while self.user_input == self.com_list:

            com = self.com_list.append(ra.randint(1, 4))
            time.sleep(1)
            return com

    def show_com_list(self):
        print("hello")

root = Tk()
app = Gui()
app.mainloop()