from tkinter import *


win = Tk()
win.geometry("800x600+300+50")
cnv = Canvas(win, width=800, height=600, highlightthickness=0, bg="black")
cnv.place(x=0, y=0)


def kill(z):
    exit()

def square(x, y, r, t, c):
    cnv.create_rectangle(x-r, y-r, x+r, y+r, fill=c, tags=str(t))

square(200, 200, 100, "obj1", "red")
square(200, 500, 100, "obj2", "green")


def print_obj_name(z):
    print(z)

def bind_loop(n):
    a = 1
    for i in range(n):
        cnv.tag_bind("obj"+str(a), "<Button-1>", print_obj_name)
        a += 1
        print("bind_set")


bind_loop(2)

win.bind("<Escape>", kill)

win.mainloop()
