from tkinter import *
import random as ra


class Gui(Frame):
    # calls all the methods when the program starts
    def __init__(self):
        Frame.__init__(self, bg="#303030")  # set window background color
        self.window()
        self.chars = "r", "b", "g", "y"
        self.user_input = []
        self.com_list = []
        self.grid()

        # creates the red button
        self.red = Button(self, bg="red", command=self.count_red)
        self.red.config(width=50, height=20)
        self.red["text"] = "Red"
        self.red.grid(row=0, column=0, padx=70, pady=70)    # sets location and space between buttons

        # creates the blue button
        self.blue = Button(self, bg="blue", command=self.count_blue)
        self.blue.config(width=50, height=20)
        self.blue["text"] = "Blue"
        self.blue.grid(row=0, column=2)

        # creates the green button
        self.green = Button(self, bg="green", command=self.count_green)
        self.green.config(width=50, height=20)
        self.green["text"] = "Green"
        self.green.grid(row=2, column=0)

        # creates the yellow button
        self.yellow = Button(self, bg="yellow", command=self.count_yellow)
        self.yellow.config(width=50, height=20)
        self.yellow["text"] = "Yellow"
        self.yellow.grid(row=2, column=2)

    def window(self):    # creates the window
        root.title("Color Blast")
        root.geometry("950x840")
        root.config(bg="#303030")

    def count_red(self):    # add r to user input
        r = self.user_input.append("r")
        self.you_win()
        return r

    def count_blue(self):    # add b to user input
        b = self.user_input.append("b")
        self.you_win()
        return b

    def count_green(self):    # add g to user input
        g = self.user_input.append("g")
        self.you_win()
        return g

    def count_yellow(self):    # add y to user input
        y = self.user_input.append("y")
        self.you_win()
        return y

    def ran_color(self):    # adds random char to com_list
        self.com_list.append(ra.choice(self.chars))
        return self.com_list

    def you_win(self):    # gets called when you click a button
        self.ran_color()
        # checks if random and com number are equal lengths
        if len(self.user_input) == len(self.com_list):
            if self.user_input == self.com_list:    # popup window if you guessed right
                top = Toplevel()
                top.geometry("150x75")
                msg = Message(top, text="Your Win this round!")
                msg.pack()
                btn = Button(top, text="On to the next level", command=top.destroy)
                btn.pack()
                self.com_list = []
                self.user_input = []
            else:    # popup window if you didn't guess the right color
                top = Toplevel()
                top.geometry("150x75")
                msg = Message(top, text="You Lose!")
                msg.pack()
                btn = Button(top, text="Retry", command=top.destroy)
                btn.pack()
                self.user_input = []
                self.com_list = []
        elif len(self.user_input) != len(self.com_list):   # resets list length just in case
            self.user_input = []
            self.com_list = []


root = Tk()
app = Gui()
app.mainloop()