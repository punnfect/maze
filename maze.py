#!/usr/bin/python3
# has to be run ./file.py will only run sudo python3 file.py
# tkinter is only attached to sudo for some reason
# will figure out why later
from graphics import Window

def main():
    win = Window(800, 600)
    win.wait_for_close()

main()
