from tkinter import *

class Vb:
    w, h = 800, 600
    a = 400
    n = 3

win = Tk()
win.minsize(Vb.w, Vb.h)

cnv = Canvas(win, width=Vb.w, height=Vb.h, highlightthickness=0)
cnv.place(x=0, y=0)

def kill(z):
    exit()

def test(z):
    print("yoo")

win.bind("<Escape>", kill)

def square(x, y, r, t):
    cnv.create_rectangle(x-r, y-r, x+r, y+r, fill="white", tags=t)

square(400, 300, 200, "main1")

cnv.tag_bind("main1", "<Button-1>", test)

def grid():
    pass

win.mainloop()