from graphics import Window
from maze import Maze



def main():
    num_rows = 30
    num_cols = 40
    margin = 50
    screen_x = 1280
    screen_y = 720
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    print("welcome to Maze Maker")
    input("press key to create Maze")

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("Maze Created")
    input("press key to Solve")
    maze.solve()
    
    print("close window to exit")
    win.wait_for_close()


main()
