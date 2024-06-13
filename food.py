#!usr/bin/env/python

### --- IMPORTS --- ###

from turtle import Turtle
import random

### --- CLASS --- ###

#were going to inherit from Turtle to make it easier to write this class
class Food(Turtle):
    #we want to init the class
    def __init__(self):
        super().__init__()

        #because we have inherited turtle we can call it's methods directly
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        #we want to call make_food whenever it get's hit by the snake
        #everytime it's within 15pixels of the food it will refresh
        self.make_food()
    
    def make_food(self):
        """Creates the food at random coords on the screen
        """
        #go to random coords
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
