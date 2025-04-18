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
            
class Cell:
        def __init__(
                  self, x1, y1, x2, y2, win,
                    has_left_wall=True, has_right_wall=True,
                      has_top_wall=True, has_bottom_wall=True
        ):
             self.x1 = x1
             self.y1 = y1
             self.x2 = x2
             self.y2 = y2
             self.win = win
             self.has_left_wall = has_left_wall
             self.has_right_wall = has_right_wall
             self.has_top_wall = has_top_wall
             self.has_bottom_wall = has_bottom_wall

        def draw(self):
            if self.has_left_wall == True:
                point1 = Point(self.x1, self.y1)
                point2 = Point(self.x1, self.y2)
                line_l_wall = Line(point1, point2)
                line_l_wall.draw(self.win.canvas, "black")
            if self.has_bottom_wall == True:
                point1 = Point(self.x1, self.y2)
                point2 = Point(self.x2, self.y2)
                line_b_wall = Line(point1, point2)
                line_b_wall.draw(self.win.canvas, "black")
            if self.has_right_wall == True:
                point1 = Point(self.x2, self.y1)
                point2 = Point(self.x2, self.y2)
                line_r_wall = Line(point1, point2)
                line_r_wall.draw(self.win.canvas, "black")
            if self.has_top_wall == True:
                point1 = Point(self.x1, self.y1)
                point2 = Point(self.x2, self.y1)
                line_t_wall = Line(point1, point2)
                line_t_wall.draw(self.win.canvas, "black")

        def draw_move(self, to_cell, undo=False):
             center_x = (self.x1 + self.x2) / 2 
             center_y = (self.y1 + self.y2) / 2
             self.center = Point(center_x, center_y)
             to_center_x = (to_cell.x1 + to_cell.x2) / 2
             to_center_y = (to_cell.y1 + to_cell.y2) / 2 
             to_cell.center = Point(to_center_x, to_center_y)   
             move_line = Line(self.center, to_cell.center)
             if undo == False:
                  move_line.draw(self.win.canvas, "red")
             if undo == True:
                  move_line.draw(self.win.canvas, "gray")     
            

class Maze:
        def __init__(
                self, x1, y1, 
                num_rows, num_cols, 
                cell_size_x, 
                cell_size_y, 
                win,
        ):
            self.x1 = x1
            self.y1 = y1
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.cell_size_x = cell_size_x
            self.cell_size_y = cell_size_y
            self.win = win
            self._create_cells()

        def _create_cells(self):
             self._cells = []
             pass
             
             
     
                 
                 
                 
                 
                  
                  
             
             
             
     