#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     26/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def main():

    #Create a defgault 200 x 200 window
    win = GraphWin("tic - Tac - Toe") #size of window can be changed by adding in x and y values next to it

    #Set coordinates to go from (0,0) in the lower left and (3,3) in the upper right
    win.setCoords(0.0,0.0,3.0,3.0)

    #Draw verical lines - side ways
    Line(Point(1,0), Point(1,3)).draw(win)
    Line(Point(2,0), Point(2,3)).draw(win)

    #Draw horizontal line - up and down
    Line(Point(0,1), Point(3,1)).draw(win)
    Line(Point(0,2), Point(3,2)).draw(win)

    win.getMouse()
    win.close()

main()