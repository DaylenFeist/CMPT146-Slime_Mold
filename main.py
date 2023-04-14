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
            which is the top sources. Thus, it is not exactly the perfect analog to the
            real life slime mold, which is often seen branching out. However, it does
            a beautiful spectacle to behold!

"""


from PIL import Image
import numpy as np
import random

WIDTH, HEIGHT = (50, 50)
TOTAL_FRAMES = 100
#MAIN LOOP
def main():
    """
    Purpose: This function's primary objective is to house all of the primary functions
    of the project.
        This includes creating the background, all the agents, creating each frame, and
        creating the gif
    Pre-Conditions: none
    Post-Contitions: creates gif in same directiory
    Return: Returns nothing
    """
    #create trail_map
    trail_map =np.zeros((HEIGHT,WIDTH), dtype=np.uint8)

    #create all agents
        #add code here

    #simulate frames,
    frames = []
    for i in range(TOTAL_FRAMES):


        #convert numpy array to pillow Image
        frames.append(Image.fromarray(trail_map))

    #convert all frames to a gif
    frames[0].save('trail_map.gif', format="GIF", append_images=frames[1:], save_all=True, loop=0)