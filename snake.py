### --- IMPORTS --- ###

#our turtle stuff
from turtle import Turtle as T

### --- CONSTANTS --- ###

#for this we use a lot of constants, constants are useful here as we can change the core of our 
#snakes creation and movement without having to dive into the code and edit anything.

#define our starting positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
#our snakes color
COLOR = "greenyellow"
#our snakes move distance
MOVE = 20
#we set these constants to control our stankes turn
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

### --- CLASS --- ###

#create our class
class Snake:
    #initialize the class
    def __init__(self) -> None:
        """Init for our snake, has attributes for segments and our snake create method
        """
        #segments list for created segements to be controlled easily
        self.segments = []
        #run create snake method
        self.create_snake()
        #set head of the snake as segment 0
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the base snake
        """
        #run a for loop for our starting positions, each position is looped throuhg and calls add segment
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def move(self):
        """Moves the snake by looping through segments, last to first, the pieces will move into 
        The space of those ahead of them
        """
        #we now loop through the segments
        for seg_num in range(len(self.segments) -1, 0, -1):
            #this loops through each segments making the last move to the one in front of it
            new_x= self.segments[seg_num - 1].xcor()
            new_y= self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        #tell the head to move the rest will follow
        self.head.forward(MOVE)

    def add_segment(self, position):
        """Creates a segment

        Args:
            position ([type]): The position we want to create the segement at
        """
        #create snake
        segment = T("square")
        segment.color(COLOR)
        #this will give it a nice square, non blocky shape
        segment.shapesize(stretch_len=0.8, stretch_wid=0.8)
        #we don't want it to draw
        segment.penup()
        #set it's position and append to segments
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        """Adds the new segment to a snake
        """
        self.add_segment(self.segments[-1].position())

    #D.24.CW - Added snake reset func to reset snake after game over
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    #these for turning our snake

    def up(self):
        """Turns snake north
        """
        #we want to do a format like this to abide to snake rules, snake shouldn't be allowed to
        #turn back on itself as that would kill it. So we make a check to see if it's going a certain way
        #that it can't turn back on itself.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        """Turns snake south
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        """turns snake left
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        """turns snake right
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)