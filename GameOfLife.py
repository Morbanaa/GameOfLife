# Game of Life
# Teddy Rodd

"""
Rules:
Survive: cell has 2-3 cells next to it
Overpop: cell dies when it has more than 3 cells next to it
Underpop: cell dies when it has less than 2 cells next to it
Birth: If an empty spot has three cells around it a new cell is made

"""

import time
import sys
import keyboard

class Cell():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos

class Pencil(Cell):
    pass


def main():
    # World Bounds
    world_height = 25
    world_width = 50

    # Creates Game Map
    world_map = world_gen(world_height,world_width)

    # Create Pencil
    pencil = Pencil(world_height//2,world_width//2)

    # Main Game Loop
    while True:
        # Prep for next frame
        clear_move_cursor()

        # Update
        draw_cells()
        update_cells()

        # Render
        render_world(world_map,world_height,world_width,pencil)

        # Controls Simulation Tick Rate
        time.sleep(.1)


# Creates game space
def world_gen(world_height,world_width):
    world_map = []
    for y in range(world_height):
        row = []
        for x in range(world_width):
            if y == 0 or y == world_height -1 or x == 0 or x == world_width -1:
                row.append("@")
            else:
                row.append(" ")
        world_map.append(row)

    return world_map


# Draws the game each frame
def render_world(world_map,world_height,world_width,pencil):
    for y in range(world_height):
        for x in range(world_width):
            if y == pencil.ypos and x == pencil.xpos:
                print("^",end="")
            else:
                print(world_map[y][x],end="")
        print()


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
