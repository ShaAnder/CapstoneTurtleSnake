#!usr/bin/env/python

### --- IMPORTS --- ###

#our turtle stuff
from turtle import Screen as S
import turtle
#import time for delays
import time

#import our snake
from snake import Snake
#import our food
from food import Food
#we also want our scoreboard
from scoreboard import Scoreboard

### --- SCREEN SETUP --- ###

#initialize screen object
scr = S()
#set the height and width
scr.setup(width=600, height=600)
#changes bg color
scr.bgcolor("black")
#adds a name to the top of the window
scr.title("Snake")
#tracer goes off so we can manually call movement
scr.tracer(0)

### --- OBJECTS --- ###

snake = Snake()
food = Food()
score = Scoreboard()

### --- LISTENERS --- ###

#we create listeners to control our boi
scr.listen()
scr.onkey(snake.up, "w")
scr.onkey(snake.down, "s")
scr.onkey(snake.left, "a")
scr.onkey(snake.right, "d")

### --- FUNCS --- ###

#D.24.CW these functions are apart of day 24's coursework, to add a highscore, be able
#to reset for replayablility and save our highscore to a file via what we learnt about
#files and directories

def play_again():
    """Resets the screen for another round
    """
    time.sleep(0.5)
    score.reset()
    time.sleep(0.5)
    scr.update()
    snake.reset()
    #we needed to add another batch of scr.listen commands into this function
    #or else the new snake does not respond to key presses
    scr.listen()
    scr.onkey(snake.up, "w")
    scr.onkey(snake.down, "s")
    scr.onkey(snake.left, "a")
    scr.onkey(snake.right, "d")

def write_scores():
    """Sets the game over state and writes the high score
    """
    score.game_over()
    #we wanna call reset here to ensure it actually get's updated before writing
    score.reset()
    #D.24.CW - Using what we have learnt to save high scores to a txt doc (not cwd so full path)
    score_save_loc = "Day20-40\Day21_Project-Snake_Game"
    with open(f"{score_save_loc}/scores.txt", mode="w") as file:
        name = turtle.textinput("Submit Your Name", "")
        file.write(f"\n{name}: {score.scores}")


### --- MAIN --- ###

#we want to setup a while loop
game_on = True
while game_on:
    #we want to delay and update the screen here
    scr.update()
    time.sleep(.2)
    #move our boi
    snake.move()
    #now we want to detect food collisions
    if snake.head.distance(food) < 15:
        #create a new piece of food
        food.make_food()
        #extend our snek
        snake.grow()
        #add to score
        score.score +=1
        score.score_point()

    #detect collision with wall 
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() <-285:
        #D.24.CW removed kill loop conditions to enable play_again unless user does not want to
        again = turtle.textinput("Play Again?", "y/n")
        if again == "y":
            play_again()
        else:
            game_on = False
            write_scores()

    #detect collision with tail, we loop through the segments past 0
    for segment in snake.segments[1:]:
        #if the snake distance is < 10 counts as collision kill the game 
        if snake.head.distance(segment) < 10:
            #D.24.CW removed kill loop conditions to enable play_again unless user does not want to
            again = turtle.textinput("Play Again?", "y/n")
            if again == "y":
                play_again()
            else:
                game_on = False
                write_scores()

### --- EXIT --- ###

scr.exitonclick()