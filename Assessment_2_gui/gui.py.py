from tkinter import *
from random import *
from time import *

class Colour:
    def __init__(self):
        self.bg = "black"
        self.button = "white"

class Score:
    def __init__(self):
        self.points = 0
        self.hund = True

    def increase(self):
        self.points += 1

    def decrease(self):
        if self.points == 0:
            return self.points
        self.points -= 1


class Tme:
    def __init__(self):
        self.t1 = None
        self.t2 = None
        self.limit = 2

    def start_time(self):
        self.t1 = time()

    def stop_time(self):
        self.t2 = time()


def hundred():
    """
    :return:doesnt return anything
    """
    can.delete(ALL)
    sky = can.create_rectangle(0, 0, 400, 350, fill="dark blue")
    sun = can.create_oval(300, 250, 360, 350, fill="yellow")
    horizon = can.create_rectangle(0, 320, 400, 400, fill="brown")
    can.tag_bind(sky, "<ButtonPress-1>", square)
    can.tag_bind(sun, "<ButtonPress-1>", square)
    can.tag_bind(horizon, "<ButtonPress-1>", square)




def ship():
    x1 = randint(1, 360)
    y1 = randint(1, 360)
    while True:
        x2 = randint(1, 360)
        y2 = randint(1, 360)
        x3 = randint(1, 360)
        y3 = randint(1, 360)
        if x2 + 40 > x1 and x2 < x1 + 40 and y1 + 40 > y2 and y1 < y2 + 40:
            continue
        if ps.points >= 50:
            if x3 + 40 > x1 and x3 < x1 + 40 and y1 + 40 > y3 and y1 < y3 + 40:
                continue
            if x3 + 40 > x2 and x3 < x2 + 40 and y2 + 40 > y3 and y2 < y3 + 40:
                continue
        break
    rec = can.create_rectangle(x1, y1, x1 + 40, y1 + 40, fill="blue")
    if ps.points >= 10:
        cir = can.create_oval(x2, y2, x2 + 40, y2 + 40, fill="green")
        can.tag_bind(cir, "<ButtonPress-1>", circle)
    if ps.points >= 50:
        rec2 = can.create_rectangle(x3, y3, x3 + 40, y3 + 40, fill="green")
        can.tag_bind(rec2, "<ButtonPress-1>", circle)
    can.tag_bind(rec, "<ButtonPress-1>", square)
    if ps.points == 100 and ps.hund:
        ps.hund = False
        hundred()
    tm.start_time()


def easy():
    tm.limit = 3
    difc.config(text="Difficulty: Easy")


def normal():
    tm.limit = 2
    difc.config(text="Difficulty: Normal")


def hard():
    tm.limit = 1
    difc.config(text="Difficulty: Hard")


def bo():
    col.bg = "black"
    col.button = "orange"
    difficulty.configure(bg=col.bg, fg=col.button)
    colour.config(bg=col.bg, fg=col.button)
    start.config(bg=col.bg, fg=col.button)
    score.config(bg=col.bg, fg=col.button)
    border.config(bg=col.bg, fg=col.button)
    difc.config(bg=col.bg, fg=col.button)


def pg():
    col.bg = "purple"
    col.button = "gold"
    difficulty.config(bg=col.bg, fg=col.button)
    colour.config(bg=col.bg, fg=col.button)
    start.config(bg=col.bg, fg=col.button)
    score.config(bg=col.bg, fg=col.button)
    border.config(bg=col.bg, fg=col.button)
    difc.config(bg=col.bg, fg=col.button)


def blu():
    window.config(bg="light blue")


def blk():
    window.config(bg="black")


def gb():
    col.bg = "grey"
    col.button = "black"
    difficulty.config(bg=col.bg, fg=col.button)
    colour.config(bg=col.bg, fg=col.button)
    start.config(bg=col.bg, fg=col.button)
    score.config(bg=col.bg, fg=col.button)
    border.config(bg=col.bg, fg=col.button)
    difc.config(bg=col.bg, fg=col.button)


def square(event):
    tm.stop_time()
    can.delete(ALL)
    t = tm.t2 - tm.t1
    if t < tm.limit:
        ps.increase()
        score.config(text="Score: " + str(ps.points))
    ship()

def circle(event):
    can.delete(ALL)
    ps.decrease()
    score.config(text="Score: " + str(ps.points))
    ship()


ps = Score()
tm = Tme()
window = Tk()
menu_bar = Menu(window)
col = Colour()
difc = Label(text="Difficulty: Normal")
window.configure(menu=menu_bar, bg=col.bg)
colour = Menu(menu_bar)
colour.add_command(label="black & orange", command=bo)
colour.add_command(label="purple & gold", command=pg)
colour.add_command(label="grey & black", command=gb)
colour.configure(activebackground="violet", activeforeground="blue")
menu_bar.add_cascade(label="Buttons", menu=colour)
difficulty = Menu(menu_bar)
difficulty.add_command(label="Easy", command=easy)
difficulty.add_command(label="Normal", command=normal)
difficulty.add_command(label="Hard", command=hard)
difficulty.configure(activebackground="violet", activeforeground="blue")
border = Menu(menu_bar)
border.add_command(label="blue", command=blu)
border.add_command(label="black", command=blk)
menu_bar.add_cascade(label="Difficulty", menu=difficulty)
menu_bar.add_cascade(label="Border", menu=border)
window.minsize(width=500, height=500)
can = Canvas(window, width=400, height=400)
start = Button(text="Play", command=ship)
score = Label(text="score: 0")
start.pack()
can.pack()
score.pack()
difc.pack(side=RIGHT)
window.mainloop()

