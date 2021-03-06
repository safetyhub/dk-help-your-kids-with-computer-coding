# despite what the book says it's actually bad practice to use either:
#from tkinter import *
#from tkinter import Tk

import tkinter

HEIGHT = 500
WIDTH = 800
window =  tkinter.Tk()
window.title('Bubble Blaster')
c = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()

ship_id = c.create_polygon(5,5,5,25,30,15,fill='red')
ship_id2 = c.create_oval(0,0,30,30,outline='red')
SHIP_RADIUS = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id,MID_X,MID_Y)
c.move(ship_id2,MID_X,MID_Y)

# don't abbreviate, it's bad style and not 'pythonic'
SHIP_SPEED = 10
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id,0,-SHIP_SPEED)
        c.move(ship_id2,0,-SHIP_SPEED)
    elif event.keysym == 'Down':
        c.move(ship_id,0,SHIP_SPEED)
        c.move(ship_id2,0,SHIP_SPEED)
    elif event.keysym == 'Left':
        c.move(ship_id,-SHIP_SPEED,0)
        c.move(ship_id2,-SHIP_SPEED,0)
    elif event.keysym == 'Right':
        c.move(ship_id,SHIP_SPEED,0)
        c.move(ship_id2,SHIP_SPEED,0)
c.bind_all('<Key>',move_ship)

import random

# adding _id to the end of a variable is not very semantic and bad practice
# (see bubbles_revised.py for a better approach)
bubble_id = list()
bubble_radius = list()
bubble_speed = list()
MIN_BUBBLE_RADIUS = 10
MAX_BUBBLE_RADIUS = 30
MAX_BUBBLE_SPEED = 10
GAP = 100

def create_bubble():
    x = WIDTH + GAP
    y = random.randint(0, HEIGHT)
    r = random.randint(MIN_BUBBLE_RADIUS, MAX_BUBBLE_RADIUS)
    id1 = c.create_oval(x-r, y-r, x+r, y+r, outline='white')
    bubble_id.append(id1)
    bubble_radius.append(r)
    bubble_speed.append(random.randint(1,MAX_BUBBLE_SPEED))

def move_bubbles():
    # the following line makes no sense based on semantics used
    # for `bubble in bubbles:` would have been so much better
    for i in range(len(bubble_id)):
        c.move(bubble_id[i], -bubble_speed[i], 0)

# the author throws in the main loop here and another import
# and constant variable that should be been grouped at the top
# plus there is no reference to the standard idiom:
# `if __name__ == '__main__':
import time
BUBBLE_CHANCE = 10
#MAIN GAME LOOP
while True:
    if random.randint(1, BUBBLE_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    window.update()
    time.sleep(0.01)
