
from window import *
from points_and_lines import *


def main():

    

    display = Window(1280, 720)
    display.draw_line(line1, "red")
    display.draw_line(line2, "black")
    display.wait_for_close()

if __name__ == "__main__":
    main()