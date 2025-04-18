
from window import *





def main():

    

    display = Window(1280, 720)
    cell = Cell(260, 540, 360, 640, display, True, True, True, True)
    cell2 = Cell(360, 540, 460, 640 , display, True, False, True, True)


    cell.draw()
    cell2.draw()
    display.wait_for_close()

if __name__ == "__main__":
    main()