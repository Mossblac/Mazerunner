
from window import *





def main():
    

    display = Window(800, 800)
    cell_start = Cell(10, 10, 60, 60, display, True, False, True, True)
    cell2 = Cell(60, 10, 110, 60 , display, False, False, True, True)
    cell_start.draw()
    cell2.draw()
    cell_start.draw_move(cell2, False)
    display.wait_for_close()

if __name__ == "__main__":
    main()