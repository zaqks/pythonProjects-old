from tkinter import *
from numpy import sort
from fmain2maths import *
from permutations import *


class Vb:
    
    rw, rh = 1366, 768
    w2, h2 = 400, 200
    w, h = 800, 600
    a = 400
    n = 2

    centers = {}

    player = ""
    computer = ""
    p_c = ""
    c_c = ""

    my_turn = False
    pc_turn = False

    running = True

    player_nums = []
    computer_nums = []

    player_win = False
    computer_win = False

    can_play = False


class Win(Tk):
    def __init__(self):
        super(Win, self).__init__()
        
        self.minsize(Vb.w, Vb.h)
        self.resizable(False, False)
        self.title("tic_tac_toe")
        self.attributes("-fullscreen", False)
        self.geometry(str(Vb.w) + "x" + str(Vb.h) + "+" + str(int((Vb.rw/2)-(Vb.w/2))) + "+" + str(int((Vb.rh/2)-(Vb.h/2))))
        self.wm_protocol(name="WM_DELETE_WINDOW", func=self.kill1) 

        self.cnv = Canvas(self, height=Vb.w, width=Vb.w, highlightthickness=0, bg="white")
        

        self.create_cnv()
        self.squares_fill()
        


        self.welcome_win = Toplevel(self, bg="white")
        
        self.welcome_win.attributes("-topmost", True)
        self.welcome_win.minsize(Vb.w2, Vb.h2)
        self.welcome_win.geometry("400x200+" + str(int((Vb.rw/2)-(Vb.w2/2))) + "+" + str(int((Vb.rh/2)-(Vb.h2/2))))
        self.welcome_win.resizable(False, False)
        self.welcome_win.overrideredirect(True)
        
        self.text1()
        self.buttons1()
        self.create_turn_lbl()

        self.welcome_win.bind("<Escape>", self.kill)
        self.bind("<Escape>", self.kill)

        win_combs_gen(Vb.n)

    def create_cnv(self):
        self.cnv.place(x=0, y=0)

    def dot(self, x, y, r):
        self.cnv.create_oval(x-r, y-r, x+r, y+r, fill="green")

    def square(self, x, y, r, t):
        self.cnv.create_rectangle(x-r, y-r, x+r, y+r, fill="grey", tags=str(t))

    def squares_fill(self):
        k = Vb.a / Vb.n
        sx, sy = (Vb.w - Vb.a + k)/2 , (Vb.h - Vb.a + k)/2
        case_tag = 1
        nx, ny = 0, 0

        "column loop" 
    
        
        for i in range(Vb.n*Vb.n + Vb.n-1):
            if nx != Vb.n and ny != Vb.n:
                self.square(sx, sy, k/2, t=case_tag)
                self.cnv.tag_bind(str(case_tag), "<Button-1>", self.detect_touch)
                Vb.centers[str(case_tag)] = [sx, sy]
                sx += k
                nx += 1
                case_tag += 1
                print(Vb.centers)

                "change row"

            else:
                ny += 1
                sy += k
                sx -= nx*k
                nx = 0

    def kill(self, z):
        self.quit()
        Vb.running = False
        exit()

    def kill1(self):
        self.quit()
        Vb.running = False
        exit()
            
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
        Vb.can_play = True

    def im_x(self):
        Vb.player = "x"
        Vb.computer = "o"
        Vb.p_c = "red"
        Vb.c_c = "blue"
        self.welcome_win.destroy()
        Vb.my_turn = True
        self.change_turn(1)
        Vb.can_play = True

    def create_turn_lbl(self):
        self.cnv.create_text((Vb.h+190)/2, (Vb.h-Vb.a)/4, text="", font=("bold", 30) ,tag="turn")

    def change_turn(self, p):
        print("turn lbl")
        if p == 1 and not Vb.player_win:
            self.cnv.itemconfig("turn", text="Your turn", fill=Vb.p_c)
            self.cnv.update()


        elif p == 2 and not Vb.computer_win:
            self.cnv.itemconfig("turn", text=" My turn ", fill=Vb.c_c)
            self.cnv.update()

    def multi_bind(self, n):
        a = 1
        for i in range(n):
            self.cnv.tag_bind(str(a), "<Button-1>", self.detect_touch)
            print("bind_set", a)
            a += 1

    def detect_touch(self, z):
        if Vb.can_play:
            if Vb.my_turn and not Vb.player_win:
                "convert to me"
                
                clicked_tag = self.cnv.gettags("current")[0]
                tag_center = Vb.centers[clicked_tag]
                print(clicked_tag)
                Vb.player_nums.append(int(clicked_tag))
                self.cnv.tag_unbind(str(clicked_tag), "<Button-1>")
                self.draw(tag_center[0], tag_center[1], Vb.player)
                self.check_winner(1)

                self.change_turn(2)
                Vb.my_turn = False

            elif not Vb.my_turn and not Vb.computer_win:
                "convert to pc"
                
                clicked_tag = self.cnv.gettags("current")[0]
                tag_center = Vb.centers[clicked_tag]
                print(clicked_tag)
                Vb.computer_nums.append(int(clicked_tag))
                self.cnv.tag_unbind(str(clicked_tag), "<Button-1>")
                self.draw(tag_center[0], tag_center[1], Vb.computer)
                self.check_winner(2)

                self.change_turn(1)
                Vb.my_turn = True

    def draw_x(self, x, y):
        k = Vb.a / Vb.n
        m = k/8
        self.cnv.create_line(x-(k/2)+m, y-(k/2)+m, x-(k/2)+k-m, y-(k/2)+k-m, fill="red", width=m)
        self.cnv.create_line(x-(k/2)+k-m,y-(k/2)+m, x-(k/2)+m, y-(k/2)+k-m, fill="red", width=m)

    def draw_o(self, x, y):
        k = Vb.a / Vb.n 
        r = k*6/16
        self.cnv.create_oval(x-r, y-r, x+r, y+r, fill=None, outline="blue", width = 15)
            
    def draw(self, x, y, p): 

        if p == "x":
            self.draw_x(x, y)

        if p == "o":
            self.draw_o(x, y)

    def check_winner(self, p):
        if p == 1:
            mlt_probs(Vb.player_nums, Vb.n)

            for i in range(len(State.mlt_perm)):
                if State.mlt_perm[i] in Ref.mlt_combs:

                    print(State.mlt_perm[i])
                    
                    cm = list(sort(State.perm__mlt_perm[State.mlt_perm[i]]))
                    print(cm)

                    if cm in Ref.combs:
                        print("1 win")


                        p1 = Vb.centers[str(cm[0])]
                        p2 = Vb.centers[str(cm[Vb.n-1])]

                        self.cnv.create_line(p1[0], p1[1], p2[0], p2[1], fill="black", width=7.5)

                        Vb.player_win = True
                        Vb.can_play = False
                        self.win_lbl(1)
                        
                        break

            State.perm.clear()
            State.mlt_perm.clear()
            
        if p == 2:
            mlt_probs(Vb.computer_nums, Vb.n)

            for i in range(len(State.mlt_perm)):
                if State.mlt_perm[i] in Ref.mlt_combs:

                    print(State.mlt_perm[i])

                    cm = list(sort(State.perm__mlt_perm[State.mlt_perm[i]]))
                    print(cm)

                    if cm in Ref.combs:
                        print("2 win")


                        p1 = Vb.centers[str(cm[0])]
                        p2 = Vb.centers[str(cm[Vb.n-1])]

                        self.cnv.create_line(p1[0], p1[1], p2[0], p2[1], fill="black", width=7.5)

                        Vb.computer_win = True
                        Vb.can_play = False
                        self.win_lbl(2)
                        break

            State.perm.clear()
            State.mlt_perm.clear()
        
    def win_lbl(self, p):
        print("win lbl")
        if p == 1:
            self.cnv.itemconfig("turn", text="  You win  ", fill=Vb.p_c)
            self.cnv.update()

        elif p == 2:
            self.cnv.itemconfig("turn", text="  I win  ", fill=Vb.c_c)
            self.cnv.update()



win = Win()
while Vb.running:
    win.update()
