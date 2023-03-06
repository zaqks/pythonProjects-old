from SnakeGame import *

win2 = Toplevel(win)
win2.attributes("-topmost", True)
win2.geometry("400x600+0+0")


def teleport_check():
    if Vb.teleport:
        Vb.teleport = False
    else:
        Vb.teleport = True


def self_eat_check():
    if Vb.can_eat_him_self:
        Vb.can_eat_him_self = False
    else:
        Vb.can_eat_him_self = True


(Button(win2, text="   UP   ", font=("bold", 20))).place(x=150, y=50)
(Button(win2, text="DOWN", font=("bold", 20))).place(x=150, y=200)
(Button(win2, text="RIGHT", font=("bold", 20))).place(x=250, y=125)
(Button(win2, text=" LEFT ", font=("bold", 20))).place(x=50, y=125)

(Checkbutton(win2, text="teleport", command=teleport_check)).place(x=50, y=300)
(Checkbutton(win2, text="collision_detection", command=self_eat_check)).place(x=50, y=325)

while Vb.playing:
    while not Vb.pause:
        win.anim()
        win2.update()
    win.update()

