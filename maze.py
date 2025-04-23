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
        self._reset_cells_visited()
        self.solve()
        
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
        time.sleep(0.02)

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
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

            
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited=False

    def solve(self):
        self._solve_r(0, 0)
           
    def _solve_r(self, i , j):
    
        self._animate()
        self._cells[i][j].visited=True
        if self._cells[-1][-1].visited==True:
            print("Maze Solved")
            return True
        else:
            right = i+1
            left = i-1
            up = j-1
            down = j+1
            if right < self._num_cols and self._cells[right][j].has_left_wall==False and self._cells[right][j].visited==False:
                self._cells[i][j].draw_move(self._cells[right][j])
                if self._solve_r(right, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[right][j], True)
            if down < self._num_rows and self._cells[i][down].has_top_wall==False and self._cells[i][down].visited==False:
                self._cells[i][j].draw_move(self._cells[i][down])
                if self._solve_r(i, down):
                    return True 
                else:
                    self._cells[i][j].draw_move(self._cells[i][down], True)
            if left >= 0 and self._cells[left][j].has_right_wall==False and self._cells[left][j].visited==False:
                self._cells[i][j].draw_move(self._cells[left][j])
                if self._solve_r(left, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[left][j], True)
            if up >= 0 and self._cells[i][up].has_bottom_wall==False and self._cells[i][up].visited==False:
                self._cells[i][j].draw_move(self._cells[i][up])
                if self._solve_r(i, up):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][up], True)
            
            
            
        



            
            


        

                
           

        