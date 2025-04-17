import tkinter as tk
import time
from tkinter import Tk, BOTH, Canvas



class Window:
        def __init__(self, width, height):
            self.root = tk.Tk()
            self.root.title("Mazerunner")
            self.canvas = tk.Canvas(self.root, width = width, height = height)
            self.canvas.pack()
            self.is_running = False
            self.root.protocol("WM_DELETE_WINDOW", self.close)

        def redraw(self):
            self.root.update_idletasks()
            self.root.update()

        def wait_for_close(self):
            self.is_running = True
            while self.is_running is True:
                self.redraw()
                time.sleep(0.01)

        def close(self):
            self.is_running = False