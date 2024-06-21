#!/usr/bin/python3
# has to be run ./file.py will only run sudo python3 file.py
# tkinter is only attached to sudo for some reason
# will figure out why later
from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.draw(1, 1, 100, 100)
    c = Cell(win)
    c.draw(100, 1, 200, 100)
    c = Cell(win)
    c.draw(200, 1, 300, 100)
    c = Cell(win)
    c.draw(300, 1, 400, 100)

    win.wait_for_close()

main()
