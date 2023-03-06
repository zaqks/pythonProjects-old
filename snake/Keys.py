from Moving import *


class Keys:

    def dev_console(z):
        if Vb.dev_console:
            Vb.dev_console = False
        else:
            Vb.dev_console = True

    def up(z):
        if not Moving.directions_state["down"] and not Vb.pause:
            Moving.directions_state["up"], Moving.directions_state["down"], Moving.directions_state["right"], Moving.directions_state["left"] = \
                True, False, False, False
            Moving.sx, Moving.sy = Moving.directions["up"]

    def down(z):
        if not Moving.directions_state["up"] and not Vb.pause:
            Moving.directions_state["up"], Moving.directions_state["down"], Moving.directions_state["right"], Moving.directions_state["left"] =\
            False, True, False, False
            Moving.sx, Moving.sy = Moving.directions["down"]

    def right(z):
        if not Moving.directions_state["left"] and not Vb.pause:
            Moving.directions_state["up"], Moving.directions_state["down"], Moving.directions_state["right"], Moving.directions_state["left"] =\
                False, False, True, False
            Moving.sx, Moving.sy = Moving.directions["right"]

    def left(z):
        if not Moving.directions_state["right"] and not Vb.pause:
            Moving.directions_state["up"], Moving.directions_state["down"], Moving.directions_state["right"], Moving.directions_state["left"] =\
                False, False, False, True
            Moving.sx, Moving.sy = Moving.directions["left"]

    def kill(z):
        Vb.pause = True
        Vb.playing = False
