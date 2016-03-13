from tkinter import *
from GUI.Color import Color


class Gui(Frame, Color):

    def __init__(self):
        Frame.__init__(self, bg="#303030")
        self.window()
        self.red_btn()
        self.green_btn()
        self.blue_btn()
        self.yellow_btn()
        self.grid()

    def window(self):
        root.title("Color Blast")
        root.geometry("950x840")
        root.config(bg="#303030")

    def red_btn(self):
        red = Button(self, bg="red")
        red.config(width=50, height=20)
        red["text"] = "Red"
        red["command"] = self.whatWhat()
        red.grid(row=0, column=0, padx=70, pady=70)

    def blue_btn(self):
        blue = Button(self, bg="blue")
        blue.config(width=50, height=20)
        blue["text"] = "Blue"
        blue["command"] = self.whatWhat()
        blue.grid(row=2, column=0)

    def green_btn(self):
        green = Button(self, bg="green")
        green.config(width=50, height=20)
        green["text"] = "Green"
        green["command"] = self.whatWhat()
        green.grid(row=0, column=2)

    def yellow_btn(self):
        yellow = Button(self, bg="yellow")
        yellow.config(width=50, height=20)
        yellow["text"] = "Yellow"
        yellow["command"] = self.whatWhat()
        yellow.grid(row=2, column=2)


root = Tk()
app = Gui()
app.mainloop()
print(Color.whatWhat)