from tkinter import *


class Vb:
    rw, rh = 1366, 768
    w2, h2 = 400, 200
    w, h = 800, 600
    a = 400
    n = 1


class Win(Tk):
    def __init__(self):
        super(Win, self).__init__()

        """main win creation"""
        self.minsize(Vb.w, Vb.h)
        self.resizable(False, False)
        self.title("tic_tac_toe")
        self.attributes("-fullscreen", False)
        self.geometry(str(Vb.w) + "x" + str(Vb.h) + "+" + str(int((Vb.rw/2)-(Vb.w/2))) + "+" + str(int((Vb.rh/2)-(Vb.h/2))))
        

        "secondary win creation"
        def sec(self):
            self.welcome_win = Toplevel(self, bg="white")
            self.welcome_win.overrideredirect(True)
            self.welcome_win.attributes("-topmost", True)
            self.welcome_win.minsize(Vb.w2, Vb.h2)
            self.welcome_win.geometry("400x200+" + str(int((Vb.rw/2)-(Vb.w2/2))) + "+" + str(int((Vb.rh/2)-(Vb.h2/2))))
            self.welcome_win.resizable(False, False)
                
                
        """canvas creation"""
        self.cnv = Canvas(self, height=Vb.w, width=Vb.w, highlightthickness=0, bg="white")
        self.cnv.place(x=0, y=0)


        """draw grid"""
        self.draw_grid()

        "click binding"
        self.cnv.tag_bind("obj1", "<Button-1>", self.yoo)

    """#################### SECONDARY FUNTIONS #################"""

    """grid functions"""
    def square(self, x, y, r, t):
        self.cnv.create_rectangle(x-r, y-r, x+r, y+r, fill=None, tags=str(t))

    def draw_grid(self):
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
                self.square(sx, sy, k/2, t="obj" + str(case_tag))
                sx += k
                nx += 1

                case_tag += 1

                "change row"

            else:
                ny += 1
                sy += k
                sx -= nx*k
                nx = 0

    def yoo(self):
        print("yoo")

win = Win()
win.mainloop()