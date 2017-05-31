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
    p = Point(50,60) #created point
    win = GraphWin() #creates graphic window - named shaped
    p.draw(win) #point drawn into window
    p2 = Point(140,100) #created point 2
    p2.draw(win) #point 2 drawn into window

    win.getMouse()
    win.close()
main()