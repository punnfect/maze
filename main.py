#!/usr/bin/python3
# has to be run ./file.py will only run sudo python3 file.py
# tkinter is only attached to sudo for some reason
# will figure out why later

from graphics import Window
from maze import Maze

def main():
    num_rows = 5
    num_cols = 5
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    maze.solve()
    win.wait_for_close()

main()
