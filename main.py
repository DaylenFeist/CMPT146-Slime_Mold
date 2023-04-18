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
            agent.change_rotation(sense(trail_map, agent))
        trail_map = update_trail_map(trail_map, agents)

        # convert numpy array to pillow Image
        frames.append(Image.fromarray(trail_map))

    # convert all frames to a gif
    frames[0].save('trail_map.gif', format="GIF", append_images=frames[1:], fps=30, save_all=True, loop=0)


def update_trail_map(trail_map, agents):
    """
    Purpose: Add Trails, Darken, Diffuse trailmap
    Pre-Conditions: np array: trail_map, list of Agent objects.
    Post-Conditions: Does not change initial variables
    Return: next frame of trail_map
    """
    new_trail_map = trail_map.copy()
    for agent in agents:
        pos_x, pos_y = agent.get_position()
        new_trail_map[round(pos_y), round(pos_x)] = 255

    newer_trail_map = new_trail_map.copy()
    for row in range(HEIGHT):
        for col in range(WIDTH):
            diffused_pixel = new_trail_map[row, col] * (1-DIFFUSE_RATE) + diffuse(new_trail_map, col, row) * DIFFUSE_RATE
            # using a second list, as we dont want the blurred array to effect the rest of the non-blurred array
            newer_trail_map[row, col] = max(0, diffused_pixel - DARKEN_RATE)

    return newer_trail_map


def diffuse(trail_map, square_x, square_y):
    """
    Purpose: Add Trails, Darken, Diffuse trailmap
    Pre-Conditions: np array: trail_map, list of Agent objects.
    Post-Conditions: Does not change initial variables
    Return: next frame of trail_map
    """

    brightness = 0
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            square_brightness = int(check_square(trail_map, square_x + x_offset, square_y + y_offset))
            brightness += square_brightness
    return np.uint8(brightness / 9)
    #returning min(255, np.uint8(brightness / 9 * 3)) outputs interesting patterns


def check_square(trail_map, index_x, index_y):
    """
    Purpose: Check the brightness of a square on the trail_map, and if it is on the outside of bounds, return 0
    Pre-Conditions: lots of stuff
    Post-Conditions: none
    Return: uint8 brightness value of square, 0 if out of bounds
    """

    if index_x > WIDTH - 1 or index_x < 0 or index_y > HEIGHT - 1 or index_y < 0:
        square_brightness = 0

    else:
        square_brightness = trail_map[index_y, index_x]
    return square_brightness

def sense(trail_map, agent):
    """
    Purpose: return an angle of an agent to turn towards a higher amount of released trails
    Pre-Condition: np uint8 array: trail_map, Agent object: agent
    Post-Condition: no changes to current variables
    Return: New angle for the agent
    """
    rotation = agent.get_rotation()
    pos_x, pos_y = agent.get_position()
    left_sniff = 0
    forward_sniff = 0
    right_sniff = 0
    for distance in range(1, SENSE_DISTANCE + 1):
        left_sniff += sense_direction(trail_map, pos_x, pos_y, rotation + SENSE_ANGLE_OFFSET, SENSE_DISTANCE)
        forward_sniff += sense_direction(trail_map, pos_x, pos_y, rotation, SENSE_DISTANCE)
        right_sniff += sense_direction(trail_map, pos_x, pos_y, rotation - SENSE_ANGLE_OFFSET, SENSE_DISTANCE)


        left_weight = max(0, left_sniff - forward_sniff)
        right_weight = max(0, right_sniff - forward_sniff)
        turn_weight = (int(left_weight) - int(right_weight)) * SENSE_ANGLE_OFFSET * 2/ (255)

        # make sure rotation doesnt get too big or too small
        rotation += turn_weight
        if rotation > np.pi * 2:
            rotation -= np.pi * 2
        if rotation < 0:
            rotation += np.pi * 2

        return rotation
def sense_direction(trail_map, pos_x, pos_y, rotation, distance):
    """
    Purpose: finds the total brightness in a line of length: distance at angle: rotation from a position
    Pre-Condition: np uint8 array: trail_map, pos_x and pos_y: integers within
    Post-Condition: no changes to current variables
    Return: New angle for the agent
    """
    new_pos_x = round(pos_x + np.cos(rotation) * distance)
    new_pos_y = round(pos_y + np.sin(rotation) * distance)
    #change out of uint8
    return int(check_square(trail_map, new_pos_x, new_pos_y))

WIDTH, HEIGHT = (100, 100)
TOTAL_FRAMES = 200
MOVE_SPEED = 1
NUM_AGENTS = 1000
DIFFUSE_RATE = .1
DARKEN_RATE = 4
SENSE_DISTANCE = 4
SENSE_ANGLE_OFFSET = np.pi/4
main()
