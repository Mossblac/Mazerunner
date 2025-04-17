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

        def draw_line(self, line, fill_color):
             line.draw(self.canvas, fill_color=fill_color)

class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

class Line:
        def __init__(self, point1, point2):
            self.p1 = point1
            self.p2 = point2

        def draw(self, canvas, fill_color):
             canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
            