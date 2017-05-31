#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     25/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def main():
    #open a graphics window called shapes
    win = GraphWin("Shapes")
    # Draw a red circle centered at point (100,100) with a radius 30
    center = Point(100,100) #create point 100,100
    circ = Circle(center, 30) #radius 30
    circ.setFill("red") #set to red
    circ.setOutline("blue") #outline colour blue
    circ.draw(win) #draw on window
    #put a textual label in the center of the circle
    label = Text(center, "red circle")
    label.draw(win)
    #Draw a square using a rectangle object
    rect = Rectangle(Point(30,30), Point(70,70))
    rect.draw(win)
    #Draw a line segment using a line object (2 points)
    line = Line(Point(20,30), Point(180,165))
    line.draw(win)
    #Draw a oval using the Oval object
    oval = Oval(Point(20,150), Point(180,199)) #2 sides of oval
    oval.draw(win)


main()