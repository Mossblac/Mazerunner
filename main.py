from graphics import Window
from maze import Maze
import sys



def main():
    num_rows = 50
    num_cols = 60
    margin = 50
    screen_x = 1280
    screen_y = 720
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    print("welcome to Maze Maker")
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("Maze Created")

    
    

    
    
    
    
    
    
    print("press 'esc' or close window to exit")
    win.wait_for_close()


main()
