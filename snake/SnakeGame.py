from Keys import *


class GameWin(Tk):
    def __init__(self):
        super(GameWin, self).__init__()
        self.sw, self.sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.attributes("-fullscreen", True)
        #self.attributes("-topmost", True)
        self.cnv = Canvas(self, width=self.sw, height=self.sh, bg=Vb.cnv_bg, highlightthickness=0)
        self.create_canvas()
        self.draw_grid()
        self.create_food()

        self.bind("<Up>", Keys.up)
        self.bind("<Down>", Keys.down)
        self.bind("<Right>", Keys.right)
        self.bind("<Left>", Keys.left)
        self.bind("<p>", self.pause)
        self.bind("<r>", self.re_init)
        self.bind("<Escape>", Keys.kill)

    def show_game_over(self):
        Vb.re_pause = False
        self.cnv.delete("pause")
        self.cnv.create_text(self.sw/2, self.sh/2, fill="yellow", text="GAME OVER", font=("bold", 60), tags="game_over")
        self.cnv.create_text(self.sw / 2, self.sh * 4 / 7, fill="yellow", text="press R to restart/ press Escape to quit", font=("bold", 15), tags="game_over")
        self.cnv.update()

    def pause(self, z):
        if not Vb.pause:
            Vb.pause = True
            self.show_paused()

        elif Vb.re_pause:
            Vb.pause = False
            self.cnv.delete("pause")

    def show_paused(self):
        self.cnv.delete("game_over")
        self.cnv.create_text(self.sw / 2, self.sh / 2, fill="yellow", text="PAUSED", font=("bold", 60), tags="pause")
        self.cnv.create_text(self.sw / 2, self.sh*4 / 7, fill="yellow", text="press P to continue/ press R to restart/ press Escape to quit", font=("bold", 15), tags="pause")
        self.cnv.update()

    def create_canvas(self):
        self.cnv.place(x=0, y=0)

    def score_lb(self):
        self.cnv.create_text(self.sw-250, 25, fill=Vb.score_color, text="SCORE", font=("bold", 20), tags="score")

    def draw_grid(self):
        if Vb.grid:
            x_l = 0
            for i in range(int(self.sw/Vb.seg)+1):
                self.cnv.create_line(x_l, 0, x_l, self.sh, fill=Vb.grid_color)
                x_l += Vb.seg
            y_l = 0
            for i in range(int(self.sh/Vb.seg)+1):
                self.cnv.create_line(0, y_l, self.sw, y_l, fill=Vb.grid_color)
                y_l += Vb.seg

    def score(self):
        self.cnv.delete("score")
        self.score_lb()
        self.cnv.create_text(self.sw-150, 25, fill=Vb.score_color, text=str(Vb.score), font=("bold", 20), tags="score")
        self.cnv.update()

    def create_food(self):
        Moving.fx = choice(range(0, int(self.sw/Vb.seg)))*Vb.seg
        Moving.fy = choice(range(0, int(self.sh/Vb.seg)))*Vb.seg
        self.cnv.create_rectangle(Moving.fx, Moving.fy, Moving.fx + Vb.seg, Moving.fy + Vb.seg, outline=Vb.food_color, fill=Vb.food_color, tags="food")

    def re_init(self, z):
        self.cnv.delete("food")
        self.cnv.delete("body")
        self.cnv.delete("score")
        self.cnv.delete("pause")
        self.cnv.delete("game_over")

        Vb.score = 0
        Moving.xc, Moving.yc = Vb.seg * choice(range(5, 15)), Vb.seg * choice(range(5, 15))
        Moving.sx, Moving.sy = Moving.directions[choice(("up", "down", "right", "left"))]
        Vb.snake_parts.clear()
        Vb.snake_coors.clear()

        self.create_food()
        Vb.re_pause = True
        Vb.pause = False

    def anim(self):

        # create_body_parts
        Vb.snake_parts.append(self.cnv.create_rectangle(Moving.xc, Moving.yc, Moving.xc + Vb.seg, Moving.yc + Vb.seg, fill=Vb.snake_color, outline=Vb.snake_color_o, tags="body"))
        Vb.snake_coors.append(Moving.xc)
        Vb.snake_coors.append(Moving.yc)

        # move head
        sleep(Vb.velocity)
        self.cnv.move(Vb.snake_parts[0], Moving.sx, Moving.sy)

        # if eat

        if Moving.xc == Moving.fx and Moving.yc == Moving.fy:
            Vb.score += Vb.score_increase
            self.cnv.delete("food")
            self.create_food()
            # add body part
            Vb.snake_parts.append(
                self.cnv.create_rectangle(Moving.xc, Moving.yc, Moving.xc + Vb.seg, Moving.yc + Vb.seg,fill=Vb.snake_color, outline=Vb.snake_color_o, tags="body"))
            Vb.snake_coors.append(Moving.xc)
            Vb.snake_coors.append(Moving.yc)

        # coords update
        Moving.xc += Moving.sx
        Moving.yc += Moving.sy

        # update tail length
        if len(Vb.snake_parts) > Vb.snake_initial_length:
            self.cnv.delete(Vb.snake_parts[0])
            del Vb.snake_parts[0]
            del Vb.snake_coors[0]
            del Vb.snake_coors[0]

        # check self eat
        if not Vb.can_eat_him_self:
            if Vb.snake_coors.__contains__(Moving.xc):
                i = Vb.snake_coors.index(Moving.xc) + 1
                if not i > len(Vb.snake_coors) - 1:
                    if Vb.snake_coors[i] == Moving.yc:
                        self.pause(None)
                        self.show_game_over()

        if Vb.teleport:
            if Moving.xc < 0:
                Moving.xc = (int(self.sw / Vb.seg))*Vb.seg
            if Moving.xc > (int(self.sw / Vb.seg))*Vb.seg:
                Moving.xc = 0
            if Moving.yc < 0:
                Moving.yc = (int(self.sh / Vb.seg))*Vb.seg
            if Moving.yc > (int(self.sh / Vb.seg))*Vb.seg:
                Moving.yc = 0

        if not Vb.teleport:
            if Moving.xc < 0 or Moving.xc > (int(self.sw / Vb.seg)) * Vb.seg or Moving.yc < 0 or Moving.yc > ((int(self.sh / Vb.seg)) * Vb.seg) - Vb.seg:
                self.pause(None)
                self.show_game_over()

        # update score
        self.score()

        # update_pause

        self.update()


win = GameWin()
