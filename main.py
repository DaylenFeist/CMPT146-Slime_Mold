"""
Title: Slime Mold
Class: CMPT-146
Instructor: Jeff Long
Creator: Daylen Feist
Date: 2032-04-13

Description:
    This project has the goal of replicating the biological organism "Slime Mold"
    Taking inspiration from the following sources:
        https://cargocollective.com/sagejenson/physarum
        https://openprocessing.org/sketch/781586/
        https://www.barradeau.com/2019/1003/
        https://www.youtube.com/watch?v=X-iSQQgOd1A&ab_channel=SebastianLague
    I intend to use the following simple rules to create this simulation.
        1) We have n agents, each of which move forward, at a speed, in a certain direction
        2) Each agent releases a trail onto the canvas. (this is what we can see)
        3) The trail (trail_map) over time will diffuse, and darken.
        4) Each agent can then turn left and right, biased by the amount of trail in
            front of it, to its left, and to its right.
    These rules should allow for the simulation of a pseudo-Slime Mold

    Additional Notes:
        If I decide to change these rules, I will leave the original rule in, and make
            an amendment
        The rules that I created were heavily based on Sage Jenson's slime mold simulation
            which is the top source. Thus, it is not exactly the perfect analog to the
            real life slime mold, which is often seen branching out. However, it does
            a beautiful spectacle to behold!

"""

from PIL import Image
import numpy as np
import Agent as ag


# MAIN LOOP
def main():
    """
    Purpose: This function's primary objective is to house all of the primary functions
    of the project.
        This includes creating the background, all the agents, creating each frame, and
        creating the gif
    Pre-Conditions: none
    Post-Conditions: creates gif in same directory
    Return: Returns nothing
    """
    # create trail_map
    trail_map = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    # create all agents
    agents = []
    for x in range(NUM_AGENTS):
        agents.append(ag.Agent(WIDTH, HEIGHT))

    # simulate frames,
    frames = []
    for i in range(TOTAL_FRAMES):
        progress = i / TOTAL_FRAMES * 100
        print(f"{round(progress, 1)}%")
        for agent in agents:
            agent.move_forward(WIDTH, HEIGHT, MOVE_SPEED)

        trail_map = update_trail_map(trail_map, agents)

        # convert numpy array to pillow Image
        frames.append(Image.fromarray(trail_map))

    # convert all frames to a gif
    frames[0].save('trail_map.gif', format="GIF", append_images=frames[1:], save_all=True, loop=0)


def update_trail_map(trail_map, agents):
    new_trail_map = trail_map.copy()
    for agent in agents:
        pos_x, pos_y = agent.position()
        new_trail_map[round(pos_y), round(pos_x)] = 255

    new_trail_map[new_trail_map <= 8] = 8
    new_trail_map -= 8
    return new_trail_map

def check_square(trail_map, index_x, index_y):
    """
    Purpose: Check the brightness of a square on the trail_map, and if it is on the outside of bounds, return 0

    """
    #find point forwards

    if index_x > WIDTH - 1 or index_x < 0 or index_y > HEIGHT - 1 or index_y < 0:
        square_brightness = 0
    else:
        square_brightness = trail_map[index_y, index_x]
    return square_brightness
WIDTH, HEIGHT = (250, 250)
TOTAL_FRAMES = 200
MOVE_SPEED = 1
NUM_AGENTS = 10000

main()
