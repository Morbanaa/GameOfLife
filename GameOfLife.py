# Game of Life
# Teddy Rodd

import time
import sys
import keyboard

class Cell():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos


def main():
    # Creates Game Map
    world_height = 25
    world_width = 50

    world_gen()

    # Main Game Loop
    while True:
        # Prep for next frame
        clear_move_cursor()

        # Update
        draw_cells()
        update_cells()

        # Render
        render_world()

        # Controls Simulation Tick Rate
        time.sleep(.1)


# Creates game space
def world_gen():
    pass


# Draws the game each frame
def render_world():
    pass


# User can create new cell objects
def draw_cells():
    pass


# Determins if cells surive, birth, death by (underpopulation or overpopulation)
def update_cells():
    pass


# Move cursor to top left of console to prep for next frame
def clear_move_cursor():
    sys.stdout.write("\033[H")
    sys.stdout.flush()


# Program Entry Point
if __name__ == "__main__":
    main()
