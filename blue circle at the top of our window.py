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
from graphics import * #import all graphics
def main():
    win = GraphWin() #creates a place on the screen where the graphics will apepear (200 x 200)
    c = Circle(Point(20,30), 10)
    c.setFill("Blue")
    c.draw(win)
   # win.close() #destroy object windows
main()