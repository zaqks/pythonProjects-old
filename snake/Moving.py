from Vb import *


class Moving:
    directions_state = {"up": False, "down": False, "right": True, "left": False}
    directions = {"up": (0, -Vb.seg), "down": (0, Vb.seg), "right": (Vb.seg, 0), "left": (-Vb.seg, 0)}

    # current position of the head
    xc, yc = Vb.seg * choice(range(5, 30)), Vb.seg * choice(range(5, 30))

    fx, fy = 0, 0

    # the step
    sx, sy = directions[choice(("up", "down", "right", "left"))]
