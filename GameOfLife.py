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
import random

class Pencil():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos


def main():
    # World Bounds
    world_height = 25
    world_width = 50

    # Creates Game Map
    world_map = world_gen(world_height,world_width)

    # Create Pencil
    pencil = Pencil(world_height//2,world_width//2)

    is_running = False

    # Main Game Loop
    while True:
        # Prep for next frame
        clear_move_cursor()

        # Update
        draw_cells(world_map,pencil)
        if is_running == True:
            # Cells only move if sim is running
            update_cells(world_map,world_height,world_width)
            # Preditors only appear if sim is running
            create_predator(world_map,world_height,world_width)
            # Only Move if Sim is running
            move_predator(world_map,world_height,world_width)


        # Pauses and Starts Sim
        if keyboard.is_pressed("B") and is_running == False:
            is_running = True
        if keyboard.is_pressed("P") and is_running == True:
            is_running = False
        
        # Restart Program
        if keyboard.is_pressed("R"):
            is_running = False
            # Rebuilds map without cells
            world_map = world_gen(world_height,world_width)

        # Render
        print("Press P to Pause/Simulation || Press B to Begin Simulation:")
        print("----------------------------------------------------------")
        render_world(world_map,world_height,world_width,pencil)

        # Controls Simulation Tick Rate
        if is_running:
            time.sleep(.1)
        else:
            time.sleep(.05)


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
            # Draws the pencil
            if y == pencil.ypos and x == pencil.xpos:
                print("^",end="")
            elif world_map[y][x] == "X":
                print(f"{GREEN}X{ENDC}",end="")
            elif world_map[y][x] == "P":
                print(f"{RED}P{ENDC}",end="")
            else: # Draws everything else
                print(world_map[y][x],end="")
        print()


# User can create new cell objects
def draw_cells(world_map,pencil):
    if (keyboard.is_pressed("W") or keyboard.is_pressed("up")) and world_map[pencil.ypos -1][pencil.xpos] != "@":
        pencil.ypos -= 1
    if (keyboard.is_pressed("S") or keyboard.is_pressed("down")) and world_map[pencil.ypos +1][pencil.xpos] != "@":
        pencil.ypos += 1
    if (keyboard.is_pressed("A") or keyboard.is_pressed("left")) and world_map[pencil.ypos][pencil.xpos -1] != "@":
        pencil.xpos -= 1
    if (keyboard.is_pressed("D") or keyboard.is_pressed("right")) and world_map[pencil.ypos][pencil.xpos +1] != "@":
        pencil.xpos += 1
      
    if keyboard.is_pressed("space"):
        world_map[pencil.ypos][pencil.xpos] = "X"

def create_predator(world_map,world_height,world_width):
    rand_num = random.randint(1,15)

    if rand_num == 2:
        world_map[random.randint(2,world_height -3)][random.randint(2,world_width -3)] = "P"


def move_predator(world_map,world_height,world_width):
    for y in range(world_height):
        for x in range(world_width):
            if world_map[y][x] == "P":
                if y == 1 or y == world_height -2 or x == 1 or x == world_width -2:
                    world_map[y][x] = " "
                if y > 2 and y < world_height -2 and x > 2 and x < world_width -2:
                    rand_y = random.randint(-1,1)
                    rand_x = random.randint(-1,1)
                    world_map[y][x] = " "
                    world_map[y + rand_y][x + rand_x] = "P"





# Determins if cells surive, birth, death by (underpopulation or overpopulation)
def update_cells(world_map,world_height,world_width):
    for y in range(2,world_height -2):
        for x in range(2,world_width -2):

            # Determins number of cells around each cell
            surounded_score = 0
            # Top Row
            if world_map[y -1][x -1] == "X":
                surounded_score += 1
            if world_map[y -1][x] == "X":
                surounded_score += 1
            if world_map[y -1][x + 1] == "X":
                surounded_score += 1
            # Middle Row
            if world_map[y][x - 1] == "X":
                surounded_score += 1
            if world_map[y][x + 1] == "X":
                surounded_score += 1
            # Bottom Row
            if world_map[y +1][x -1] == "X":
                surounded_score += 1
            if world_map[y +1][x] == "X":
                surounded_score += 1
            if world_map[y +1][x + 1] == "X":
                surounded_score += 1

            predator = False
            # Top Row
            if world_map[y -1][x -1] == "P":
                predator = True
            if world_map[y -1][x] == "P":
                predator = True
            if world_map[y -1][x + 1] == "P":
                predator = True
            # Middle Row
            if world_map[y][x - 1] == "P":
               predator = True
            if world_map[y][x + 1] == "P":
                predator = True
            # Bottom Row
            if world_map[y +1][x -1] == "P":
                predator = True
            if world_map[y +1][x] == "P":
                predator = True
            if world_map[y +1][x + 1] == "P":
                predator = True

            if world_map[y][x] == "X":        
                # Underpop
                if surounded_score < 2:
                    world_map[y][x] = " "

                # Overpop
                if surounded_score > 3:
                    world_map[y][x] = " "

                # Survives if == 2-3

                # Killed Creates new predator
                if predator == True:
                    world_map[y][x] = "P"

            # Cells Breed
            if world_map[y][x] == " ":
                if surounded_score == 3:
                    world_map[y][x] = "X"
            
            # Predator Starves
            if world_map[y][x] == "P":
                if surounded_score < 6 and predator == False:
                    world_map[y][x] = " "

            



# Move cursor to top left of console to prep for next frame
def clear_move_cursor():
    sys.stdout.write("\033[H")
    sys.stdout.flush()


# Colors
RED          = '\033[31m'
GREEN        = '\033[32m'
# Reset Color
ENDC = '\033[0m'


# Program Entry Point
if __name__ == "__main__":
    main()
