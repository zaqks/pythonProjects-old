from tkinter import *
from numpy import sort
from fmain2maths import *
from permutations import *


class Vb:
    
    rw, rh = 1366, 768
    w2, h2 = 400, 200
    w, h = 800, 600
    a = 400
    n = 3

    centers = {}

    player = ""
    computer = ""
    p_c = ""
    c_c = ""

    my_turn = False
    pc_turn = False

    game_end = False

    running = True

    player_nums = []
    computer_nums = []



class Win(Tk):
    def __init__(self):
        super(Win, self).__init__()
        self.minsize(Vb.w, Vb.h)
        self.resizable(False, False)
        self.title("tic_tac_toe")
        self.attributes("-fullscreen", False)
        self.geometry(str(Vb.w) + "x" + str(Vb.h) + "+" + str(int((Vb.rw/2)-(Vb.w/2))) + "+" + str(int((Vb.rh/2)-(Vb.h/2))))
        
        self.cnv = Canvas(self, height=Vb.w, width=Vb.w, highlightthickness=0, bg="white")
        self.cnv.place(x=0, y=0)

        self.wm_protocol(name="WM_DELETE_WINDOW", func=self.kill1) 
        self.bind("<Escape>", self.kill)

        """create second window"""

        self.welcome_win = Toplevel(self, bg="white")
        self.welcome_win.overrideredirect(True)
        self.welcome_win.attributes("-topmost", True)
        self.welcome_win.minsize(Vb.w2, Vb.h2)
        self.welcome_win.geometry("400x200+" + str(int((Vb.rw/2)-(Vb.w2/2))) + "+" + str(int((Vb.rh/2)-(Vb.h2/2))))
        self.welcome_win.resizable(False, False)
        
        self.text1()
        self.buttons1()
        self.create_turn_lbl()


    def kill(self, z):
        self.quit()
        Vb.running = False
        exit()

    def kill1(self):
        self.kill("z")

               
    def buttons1(self):
        btn1 = Button(self.welcome_win, text="X", relief="flat", foreground="red", font=("bold", 40), command=self.im_x)
        btn1.place(x=400/8+20 , y=80)
        btn2 = Button(self.welcome_win, text="O", relief="flat", foreground="blue", font=("bold", 40), command=self.im_o)
        btn2.place(x=400*6/8-20, y=80)

    def text1(self):
        cnv2 = Canvas(self.welcome_win, height=50, width=300, highlightthickness=0, bg="white")
        cnv2.place(x=50, y=10)
        cnv2.create_text(155, 25, font=("bold", 15), justify="center", text="Choose your symbol:")
    
    def im_o(self):
        Vb.player = "o"
        Vb.computer = "x"
        Vb.p_c = "blue"
        Vb.c_c = "red"
        self.welcome_win.destroy()
        Vb.my_turn = True
        self.change_turn(1)

    def im_x(self):
        Vb.player = "x"
        Vb.computer = "o"
        Vb.p_c = "red"
        Vb.c_c = "blue"
        self.welcome_win.destroy()
        Vb.my_turn = True
        self.change_turn(1)

    def create_turn_lbl(self):
        self.cnv.create_text((Vb.h+190)/2, (Vb.h-Vb.a)/4, text="", font=("bold", 30) ,tag="turn")



win = Win()
while Vb.running:
    win.update()