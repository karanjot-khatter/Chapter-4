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
    win = GraphWin("Archery target",300,300)
    center = Point(150,150)
    #radius reduce by 20 each time
    white = Circle(center,100) #furtherest away - later objects will appear ontop of earlier
    white.setFill("white")
    white.draw(win)

    black = Circle(center,80)
    black.setFill("black")
    black.draw(win)

    blue = Circle(center,60)
    blue.setFill("blue")
    blue.draw(win)

    red = Circle(center,40)
    red.setFill("red")
    red.draw(win)

    yellow = Circle(center,20) #nearer to center
    yellow.setFill("yellow")
    yellow.draw(win)

    win.getMouse() #when clicked
    win.close() #close program


main()