#!usr/bin/env/python

### --- IMPORTS --- ###

#were importing turtle for inheritance

from turtle import Turtle

### --- CONSTANTS --- ###

SCORE_FONT = ('Arial', 12, 'bold')
ALIGNMENT = 'center'

### --- CLASS --- ###

class Scoreboard(Turtle):
    #let's init our score
    def __init__(self) -> None:
        super().__init__()
        #setting for the actual score
        self.score = 0
        #D24.CW adding a scores attribute for recording highscore / scores later
        self.scores = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.score_point()
        

    def score_point(self):
        """Changes the score based on food collected
        """
        #clear current score
        self.clear()
        #go to score position
        self.goto(0, 280)
        #set our message (#D.24.CW updated to reflect highscore)
        self.message = f"Score: {self.score} High Score: {self.scores}"
        #write the message
        self.write(self.message, move=False, align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        """Generates the game over message
        """
        #go to middle of screen
        self.goto(0, 0)
        #write our game over message
        self.write("Game Over", align=ALIGNMENT, font=SCORE_FONT)
        self.goto(0, -20)
        self.write(f"Your High Score was: {self.scores}", align=ALIGNMENT, font=SCORE_FONT)


    def reset(self):
        """Resets the score and updates high score
        """
        #D.24.CW Reset func
        if self.score > self.scores:
            self.scores = self.score
        self.score = 0
        self.score_point()