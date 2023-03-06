from os import kill
from tkinter import *

class Vb:
    w, h = 800, 600

class Win(Tk):
    def __init__(self):
        super(Win, self).__init__()
        self.minsize(Vb.w, Vb.h)

        self.cnv = Canvas(self, width=Vb.w, height=Vb.h, highlightthickness=0)
        self.cnv.place(x=0, y=0)

        self.bind("<Escape>", self.kill)
        self.square(100, 100, 50, "1")
        self.cnv.tag_bind("1", "<Button-1>", self.kill)

    def square(self, x, y, r, t):
        self.cnv.create_rectangle(x-r, y-r, x+r, y+r, fill=None, tags=str(t))

    def kill(self, z):
        exit()

    

win = Win()
win.mainloop()