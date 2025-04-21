from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self.visited =[]
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        
        if seed:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        open = self._cells[0][0]
        exit = self._cells[-1][-1]
        open.has_left_wall = False
        self._draw_cell(0, 0)
        exit.has_right_wall = False
        self._draw_cell(
            (self._num_cols -1), (self._num_rows -1)
        )
        
    def _break_walls_r(self, i, j):
        self.visited.append(self._cells[i][j])
        while True:
            adjacent_cells = []
            left_cell = i - 1
            right_cell = i + 1
            top_cell = j - 1
            bottom_cell = j + 1
            if left_cell >= 0 and left_cell < self._num_cols:
                if self._cells[i][j].has_left_wall:
                    adjacent_cells.append("l")
            if right_cell >= 0 and right_cell < self._num_cols:
                if self._cells[i][j].has_right_wall:
                    adjacent_cells.append("r")
            if bottom_cell >= 0 and bottom_cell < self._num_rows:
                if self._cells[i][j].has_bottom_wall:
                    adjacent_cells.append("b")
            if top_cell >= 0 and top_cell < self._num_rows:
                if self._cells[i][j].has_top_wall:
                    adjacent_cells.append("t")

             
            if len(adjacent_cells) == 0:
                self._draw_cell(i, j)
                
                return 
                
            
                
            else:
                rand_num = random.randrange(len(adjacent_cells))
                

            if adjacent_cells[rand_num] == "l":
                if self._cells[left_cell][j] not in self.visited:
                    self._cells[i][j].has_left_wall=False
                    self._draw_cell(i, j)
                    self._cells[left_cell][j].has_right_wall=False
                    self._draw_cell(left_cell, j)
                    self._break_walls_r(left_cell, j)

            if adjacent_cells[rand_num] == "r":
                if self._cells[right_cell][j] not in self.visited:
                    self._cells[i][j].has_right_wall=False
                    self._draw_cell(i, j)
                    self._cells[right_cell][j].has_left_wall=False
                    self._draw_cell(right_cell, j)
                    self._break_walls_r(right_cell, j)

            if adjacent_cells[rand_num] == "t":
                if self._cells[i][top_cell] not in self.visited:
                    self._cells[i][j].has_top_wall=False
                    self._draw_cell(i, j)
                    self._cells[i][top_cell].has_bottom_wall=False
                    self._draw_cell(i, top_cell)
                    self._break_walls_r(i, top_cell)

            if adjacent_cells[rand_num] == "b":
                if self._cells[i][bottom_cell] not in self.visited:
                    self._cells[i][j].has_bottom_wall=False
                    self._draw_cell(i, j)
                    self._cells[i][bottom_cell].has_top_wall=False
                    self._draw_cell(i, bottom_cell)
                    self._break_walls_r(i, bottom_cell)

            
                
        
            
                
           

        