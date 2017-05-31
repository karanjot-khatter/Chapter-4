#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     30/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(75,75),Point(125,125))
    shape.setOutline("Red")
    shape.setFill("Red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        #draw the rectangle - need 2 points again
        tx = p.getX()-25 #top x left and up 25
        ty = p.getY()-25 #top y up down 25
        bx = p.getX()+25 #bottom x - right 25
        by = p.getY()+25 # bottom y- up 25

    #with both point “Top Left” and “Bottom Right” then I can create square center from each click.
        Rectangle(Point(tx,ty),Point(bx,by)).draw(win)

    Text(Point(100,100),'Click again to quit!').draw(win)
    win.getMouse()
    win.close()
main()
