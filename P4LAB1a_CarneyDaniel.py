#Daniel Carney
#CTI-110
#P4LAB1a - Drawing a square and triangle using turtle graphics, except I kept deciding to get unnecessarily fancy
#2023-10-26

#set up turtle object (import and create global turtle object)

#square function:
#   for range of 4:
#       move forward 50
#       rotate 90

#triangle function:
#   for range of 3:
#       move forward 100
#       rotate 120

#actually no. i can do this cooler
#generalized polygon function(edge length, num. of edges):
#   if num. of edges < 1:
#       print("that won't work*, what are you doing")
#   else:
#       for range of (num. edges):
#           move forward (edge length)
#           rotate (360 / num. edges)
#*yes, I'm letting it have have 1 or 2 edges, it will just draw a line, and
# then with 2 edges it will return to the start of the shape like with all
# the actual polygons with higher edge count

#main function:
#   set run value to y
#   while run value is y:
#       move cursor to left
#       call fun randomize color function
#       call polygon function(50, 4)
#       move cursor to right
#       call fun randomize color function
#       call polygon function(100, 3)
#       ask user if program should run again, set run value

#fun randomize color function:
#   set r to random value between 0 and 1
#   set g to random value between 0 and 1
#   set b to random value between 0 and 1

import turtle
import random
win = turtle.Screen()
global t
t = turtle.Turtle()

def main():
    run = 'y'
    while run == 'y':
        t.penup()
        t.goto(-100, 0)
        randomizeColor()
        polygon(50, 4)
        t.goto(100, 0)
        randomizeColor()
        polygon(100, 3)
        run = input('Do you want to run the program again? y/n:')
    print('Ok, bye!')

def polygon(edge_length, num_edges):
    if num_edges < 1:
        print('Cannot have polygon with 0 or fewer edges')
    else:
        t.pendown()
        for n in range(num_edges):
            t.forward(edge_length)
            t.left(360 / num_edges)
        t.penup()

def randomizeColor():
    #I'm getting carrieed away a bit now aren't I
    #anyways the reason I'm doing this weir div. by 255 thing is at first I assumed you could put in rgb values using 0-255
    #but actually it has to be between 0 and 1, and I actually don't know how else to do that other than to divide a nice big random integer, so I kept the 255 part
    #also I kinda copied this bit from me messing around with turtle that time Norris substituted
    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255
    t.pencolor(r, g, b)

main()
