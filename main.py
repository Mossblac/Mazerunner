
from window import *





def main():
    

    display = Window(1280, 720)
    cell_start = Cell(10, 10, 110, 110, display, True, False, True, True)
    cell2 = Cell(110, 10, 210, 110 , display, False, False, True, True)
    cell_start.draw()
    cell2.draw()
    cell_start.draw_move(cell2, False)
    display.wait_for_close()

if __name__ == "__main__":
    main()