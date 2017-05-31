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
    print("This program creates 2 circles - 20 distance apart")
    #Program creates 2 circles - 20 distance apart - 2
    win = GraphWin ("Circle")
    leftEye = Circle(Point(80,50),5)
    leftEye.setFill("yellow")
    leftEye.setOutline("red")
    leftEye.draw(win)
    rightEye = Circle(Point(100,50), 5)
    rightEye.setFill("yellow")
    rightEye.setOutline("red")
    rightEye.draw(win)
main()