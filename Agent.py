import random
import numpy as np


class Agent(object):
    def __init__(self, width, height):
        """
        Purpose: Initialize an Agent Object
        Pre-Conditions: width and height which describe the width and height of canvas
        Post-Conditions: Initializes all variables related to Agent
        Return: Nothing
        """
        self.pos_x = random.randint(width/2 -25, width/2+25)
        self.pos_y = random.randint(height/2-25, height/2+25)
        self.rotation = random.random() * 2 * np.pi

    def move_forward(self, width, height, move_speed):
        """
        Purpose: Moves the agent forward according to its move speed
        Pre-Conditions:
        int width, height: describes the width and height of canvas.
        int move_speed: speed that the agent moves
        Post-Conditions: Updates x and y position of agent, and if agent hits bounding box, rotation
        Return: Nothing
        """
        self.pos_x += np.cos(self.rotation) * move_speed
        self.pos_y += np.sin(self.rotation) * move_speed

        #if out of bounds
        if self.pos_x < 0 or self.pos_y < 0 or self.pos_x > width - 1 or self.pos_y > height - 1:
            #print(self.__str__())
            #do a random bounce, maybe change to a real bounce?
            self.rotation = random.random() * 2 * np.pi
            #place on the nearest edge, or if already within the bounds, keep in same spot
            self.pos_x = min(width-1, max(0,self.pos_x))
            self.pos_y = min(height-1, max(0,self.pos_y))
            #print(self.__str__())
    def position(self):
        """
        Purpose: Moves the agent forward according to its move speed
        Pre-Conditions:
        Post-Conditions: None
        Return: x and y position of Agent
        """
        return self.pos_x, self.pos_y

    def __str__(self):
        return f"X:{self.pos_x}|Y:{self.pos_y}|Rotation:{self.rotation}"