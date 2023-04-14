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

WIDTH, HEIGHT = (50, 50)
TOTAL_FRAMES = 100
MOVE_SPEED = 1
NUM_AGENTS = 10
#MAIN LOOP
def main():
    """Added
    framework
    for Agents:
        -Created
        Class
    -Created
    movement, which
    moves in the
    agent
    's direction, if it is outside the bounding box, the direction will be created"""
    """
    Purpose: This function's primary objective is to house all of the primary functions
    of the project.
        This includes creating the background, all the agents, creating each frame, and
        creating the gif
    Pre-Conditions: none
    Post-Conditions: creates gif in same directory
    Return: Returns nothing
    """
    #create trail_map
    trail_map =np.zeros((HEIGHT,WIDTH), dtype=np.uint8)

    #create all agents
    agents = []
    for x in range(NUM_AGENTS):
        agents.append(ag.Agent(WIDTH,HEIGHT))

    #simulate frames,
    frames = []
    for i in range(TOTAL_FRAMES):
        for single_agent in agents:
            single_agent.move_forward(WIDTH,HEIGHT,MOVE_SPEED)
        
        #convert numpy array to pillow Image
        frames.append(Image.fromarray(trail_map))

    #convert all frames to a gif
    frames[0].save('trail_map.gif', format="GIF", append_images=frames[1:], save_all=True, loop=0)

main()