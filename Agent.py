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
        self.__pos_x = random.randint(width/2 -25, width/2+25)
        #self.__pos_x = width/2
        self.__pos_y = random.randint(height/2-25, height/2+25)
        #self.__pos_y = height/2
        self.__rotation = random.random() * 2 * np.pi

    def move_forward(self, width, height, move_speed):
        """
        Purpose: Moves the agent forward according to its move speed
        Pre-Conditions:
        int width, height: describes the width and height of canvas.
        int move_speed: speed that the agent moves
        Post-Conditions: Updates x and y position of agent, and if agent hits bounding box, rotation
        Return: Nothing
        """
        self.__pos_x += np.cos(self.__rotation) * move_speed
        self.__pos_y += np.sin(self.__rotation) * move_speed

        #if out of bounds
        if self.__pos_x < 0 or self.__pos_y < 0 or self.__pos_x > width - 1 or self.__pos_y > height - 1:
            #print(self.____str__())
            #do a random bounce, maybe change to a real bounce?
            self.__rotation = random.random() * 2 * np.pi
            #place on the nearest edge, or if already within the bounds, keep in same spot
            self.__pos_x = min(width-1, max(0,self.__pos_x))
            self.__pos_y = min(height-1, max(0,self.__pos_y))
            #print(self.____str__())
    def get_position(self):
        """
        Purpose: return x and y position
        Pre-Conditions:
        Post-Conditions: None
        Return: x and y position of Agent
        """
        return self.__pos_x, self.__pos_y
    def get_rotation(self):
        """
        Purpose: returns rotation
        Pre-Conditions:
        Post-Conditions: None
        Return: rotation of agent
        """
        return self.__rotation
    def change_rotation(self, rotation):
        """
        Purpose: allow outside scripts to change rotation of agent
        Pre-Conditions: int: rotation from 0, 2pi
        Post-Conditions: changes rotation of agent
        Return: none
        """
        self.__rotation = rotation
    def __str__(self):
        return f"X:{self.__pos_x}|Y:{self.__pos_y}|Rotation:{self.__rotation}"