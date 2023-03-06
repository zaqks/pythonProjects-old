import pyautogui as pg
from time import sleep

c = 5

while c!= 0:
    print(c)
    sleep(1)
    c -= 1

x1 =  1607
y1 =  567


x2 =  1607
y2 =  818



pg.moveTo(x1, y1)
pg.doubleClick(x1, y1)
pg.typewrite("yoo")
pg.click(x2, y2)