
from window import *





def main():
    

    display = Window(805, 805)
    cell_start = Cell(5, 5, 55, 55, display, True, False, True, True)
    cell2 = Cell(55, 5, 105, 55 , display, False, False, True, True)
    cell_start.draw()
    cell2.draw()
    cell_start.draw_move(cell2, False)
    display.wait_for_close()

if __name__ == "__main__":
    main()