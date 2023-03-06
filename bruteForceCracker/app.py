from tkinter import *

win = Tk()

win.geometry("800x600+0+0")

cnv = Canvas(win, height=600, width=800,background="grey",  highlightthickness=0)
cnv.place(x=0, y=0)


def kill(z):
    win.quit()
    exit()

win.bind("<Escape>", kill)


(Button(win, pady=50, padx=100, text="Login", border= None, borderwidth=0,)).place(x=250, y=125)

win.mainloop()