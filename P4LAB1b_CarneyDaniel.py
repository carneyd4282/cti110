# Daniel Carney
# CTI 110
# 2023-10-31
# P4LAB1b - Drawing Initials with Turtle Graphics

# import turtle
# create turtle object
# set pen color
# call drawText('DC', 100, 'orange', 3) function

# define drawText(string, text_size, space_size, pen_color, pen_size) function:
#   start_x = -1 * ((len(string) * text_size) + ((len(string) - 1) * space_size) * 0.5
#   start_y = -1 * text_size (height of text will be 2 * text_size, so this centers it)
#   pen up
#   go to start_x, start_y
#   set pen color to pen_color
#   set pen size to pen_size
#   for x_char in string:
#       if x_char is 'D':
#           go to 0x, 0y
#           pen down
#           go to 0x, 2y
#           go to 0.5x, 2y
#           go to 1x, 1.5y
#           go to 1x, 0.5y
#           go to 0.5x, 0.5y
#           go to 0x, 0y
#       if x_char is 'C':
#           go to 1x, 0y
#           pen down
#           go to 0.5x, 0y
#           go to 0x, 0.5y
#           go to 0x, 1.5y
#           go to 0.5x, 2y
#           go to 2x, 2y
#       pen up
#       add space and text size to start_x

import turtle
win = turtle.Screen()
global t
t = turtle.Turtle()

# why am I bothering to do this so overcomplicated? good question
# To be honest, this isn't my first class on this and this stuff is fun- it's hard to hold back from showing off just a little
# though neither this code nor my knowledge of python is really that much more advanced than what's been covered in class
# like, I understand what it means a little, but I couldn't make this object-oriented or anything like that
# (does python even support that?)

def drawText(string, text_size, space_size, pen_color, pen_size):
    start_x = -1 * ((len(string) * text_size) + ((len(string) - 1) * space_size)) * 0.5
    start_y = -1 * text_size
    t.penup()
    t.goto(start_x, start_y)
    t.pencolor(pen_color)
    t.pensize(pen_size)
    for x_char in string:
        if x_char == 'D':
            t.goto(start_x, start_y)
            t.pendown()
            t.goto(start_x, (start_y + (2 * text_size)))
            t.goto((start_x + (0.5 * text_size)), (start_y + (2 * text_size)))
            t.goto((start_x + (1 * text_size)), (start_y + (1.5 * text_size)))
            t.goto((start_x + (1 * text_size)), (start_y + (0.5 * text_size)))
            t.goto((start_x + (0.5 * text_size)), start_y)
            t.goto(start_x, start_y)
        elif x_char == 'C':
            t.goto((start_x + (1 * text_size)), start_y)
            t.pendown()
            t.goto((start_x + (0.5 * text_size)), start_y)
            t.goto(start_x, (start_y + (0.5 * text_size)))
            t.goto(start_x, (start_y + (1.5 * text_size)))
            t.goto((start_x + (0.5 * text_size)), (start_y + (2 * text_size)))
            t.goto((start_x + (1 * text_size)), (start_y + (2 * text_size)))
        else:
            print("yeah I'm not doing the whole alphabet or anything that isn't my initials")
            print("but I still made it so that I COULD add that, which is already more than I had to")
        # now I'm wondering, does python have switch statements?
        # I haven't really used them much but I am aware of them in other languages
        # for a 26+ case decision like this it would be a very slightly cleaner way to do this
        # (or at least like this would be if I was doing more than 2 characters)
        t.penup()
        start_x += text_size + space_size

drawText('DC',100,50,'orange',3)
print('done!')
