from tkinter import *


class Vb:
    rw, rh = 1366, 768
    w2, h2 = 400, 200
    w, h = 800, 600
    a = 400
    n = 3



"""###################################"""
"""main win creation"""

win = Tk()

win.minsize(Vb.w, Vb.h)
win.resizable(False, False)
win.title("tic_tac_toe")
win.attributes("-fullscreen", False)
win.geometry(str(Vb.w) + "x" + str(Vb.h) + "+" + str(int((Vb.rw/2)-(Vb.w/2))) + "+" + str(int((Vb.rh/2)-(Vb.h/2))))

"secondary win creation"
def sec(win):
    win.welcome_win = Toplevel(win, bg="white")
    win.welcome_win.overrideredirect(True)
    win.welcome_win.attributes("-topmost", True)
    win.welcome_win.minsize(Vb.w2, Vb.h2)
    win.welcome_win.geometry("400x200+" + str(int((Vb.rw/2)-(Vb.w2/2))) + "+" + str(int((Vb.rh/2)-(Vb.h2/2))))
    win.welcome_win.resizable(False, False)


"""canvas creation"""
cnv = Canvas(win, height=Vb.w, width=Vb.w, highlightthickness=0, bg="white")
cnv.place(x=0, y=0)                

def square(x, y, r, t):
    cnv.create_rectangle(x-r, y-r, x+r, y+r, fill=None, tags=str(t))

def wazzup(z):
    print("yooo")

"""grid sequence"""
def draw_grid():
    "square r"
    k = Vb.a / Vb.n

    "first center"
    sx, sy = (Vb.w - Vb.a + k)/2 , (Vb.h - Vb.a + k)/2
    case_tag = 1

    "number of line components/ lines"
    nx, ny = 0, 0

    "column loop" 


    for i in range(Vb.n*Vb.n + Vb.n-1):
        if nx != Vb.n and ny != Vb.n:
            square(sx, sy, k/2, t="obj" + str(case_tag))
            cnv.tag_bind("obj" + str(case_tag), "<Button-1>", wazzup)
            sx += k
            nx += 1

            case_tag += 1

            "change row"

        else:
            ny += 1
            sy += k
            sx -= nx*k
            nx = 0

"""grid drawing"""
draw_grid()





win.mainloop()