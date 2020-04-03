#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from macros import *

# CANVAS VARIABLES
__canvas = None
__root = None
WIDTH = 400
HEIGHT = 400

# COLOR MODE VARIABLES
__color_modes = [RGB, HSB]
__color_mode = RGB

# TRANSLATE VARIABLES
__x_offset = 0
__y_offset = 0

# STROKE/FILL VARIABLES
__stroke = BLACK
__stroke_width = 1
__fill = ''

# RECTANGLE VARIABLES
__rectangle_modes = [CORNER, CORNERS, CENTER, RADIUS]
__rectangle_mode = CORNER

#
#   CANVAS FUNTIONS
#

# Create a new window with a title
def create_window(title='Window'):
    global __root
    __root = tkinter.Tk()
    __root.title(title)

# Create a new canvas object and set the height/width
def create_canvas(w=400, h=400):
    global HEIGHT
    global WIDTH
    global __canvas
    __canvas = tkinter.Canvas(__root, width=w, height=h, bg='WHITE')
    WIDTH = w
    HEIGHT = h
    __canvas.pack()

# Sets the background to a color
def set_background(x, y=None, z=None):
    __canvas.config(bg=color(x, y, z))

# Refreshes the canvas (by deleting all the elements)
def refresh_canvas():
    __canvas.delete('all')

# Updates the canvas with newly added elements
def update_canvas():
    __root.update()

# Returns the Tkinter canvas object
def get_canvas():
    return __canvas

# Returns the Tkinter root object
def get_root():
    return __root

# Sets the x,y position as the new reference point
def translate(x, y):
    global __x_offset
    global __y_offset
    __x_offset = x
    __y_offset = y

#
#   COLOR FUNCTIONS
#

# Returns a hexadecimal color code
# Accepted imputs: Hex color code, grayscale value, RGB values, HSB values
def color(x, y, z):
    global __color_mode
    if isinstance(x, str):
        return x
    elif y is None and z is None:
        return __grayscale_to_hex(x)
    elif __color_mode == RGB:
        return __rgb_to_hex(x, y, z)

# Changes the current color mode
def color_mode(mode):
    global __color_mode
    if mode not in __color_modes:
        return
    __color_mode = mode

#
#   STROKE/FILL FUNNCTIONS
#

# Sets the color of a stroke (line or outline)
def stroke(x, y=None, z=None):
    global __stroke
    __stroke = color(x, y, z)

# Sets the thickness of a stroke (line or outline)
def stroke_width(w):
    global __stroke_width
    __stroke_width = w

def fill(x, y=None, z=None):
    global __fill
    if x is None:
        __fill = ''
    else:
        __fill = color(x, y, z)

#
#   LINE FUNCTIONS
#

# Draws a line from x1,y1 to x2,y2
def line(x1, y1, x2, y2):

    # add the translated x,y values
    x1 = x1 + __x_offset
    y1 = y1 + __y_offset
    x2 = x2 + __x_offset
    y2 = y2 + __y_offset

    # draw the line
    __canvas.create_line(x1, y1, x2, y2, fill=__stroke, width=__stroke_width)

#
#   RECTANGLE FUNCTIONS
#

# Draws a rectangle based on the current rectangle mode
def rectangle(x1, y1, x2, y2):
    global __fill, __rectangle_mode
    if __rectangle_mode == 'CORNER':
        a = x1 + __x_offset
        b = y1 + __y_offset
        c = x1 + x2 + __x_offset
        d = y1 + y2 + __y_offset
    elif __rectangle_mode == 'CORNERS':
        a = x1 + __x_offset
        b = y1 + __y_offset
        c = x2 + __x_offset
        d = y2 + __y_offset
    elif __rectangle_mode == 'CENTER':
        a = x1 - x2 / 2 + __x_offset
        b = y1 - y2 / 2 + __y_offset
        c = x1 + x2 / 2 + __x_offset
        d = y1 + y2 / 2 + __y_offset
    else:
        return
    __canvas.create_rectangle(a, b, c, d, fill=__fill,
                              outline=__stroke, width=__stroke_width)

# Sets the current rectangle mode
# CORNER  -> x1,y1 - starting point | x2 - width | y2 - height
# CORNERS -> x1,y1 - starting point | x2,y2 ending point
# CENTER  -> x1,y1 - center of rectangle | x2 - width | y2 - height
def rectangle_mode(mode):
    global __rectangle_mode, __rectangle_modes
    if mode not in __rectangle_modes:
        return
    __rectangle_mode = mode

#
#   MODULE FUNCTIONS
#

# Return a hex value based on a grayscale input
def __grayscale_to_hex(g):
    return '#{0:02x}{1:02x}{2:02x}'.format(max(0, min(g, 255)), max(0,
            min(g, 255)), max(0, min(g, 255))).upper()

# Return a hex value based on an RGB input
def __rgb_to_hex(r, g, b):
    return '#{0:02x}{1:02x}{2:02x}'.format(max(0, min(r, 255)), max(0,
            min(g, 255)), max(0, min(b, 255))).upper()
