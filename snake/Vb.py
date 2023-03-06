from tkinter import *
from time import sleep
from random import choice


class Vb:
    cnv_bg = "black"
    grid_color = "white"
    snake_color = "green"
    snake_color_o = "green"
    food_color = "red"
    score_color = "yellow"

    grid = False
    seg = 10
    velocity = seg/400

    playing = True
    pause = False

    snake_parts = []
    snake_coors = []

    snake_initial_length = 100

    can_eat_him_self = True

    score = 0
    score_increase = 10

    teleport = False

    re_pause = True

    dev_console = False
