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
    print("This program creates 2 circles using clones")
    win = GraphWin("clones")
    leftEye = Circle(Point(80,50), 5)
    leftEye.setFill("yellow")
    leftEye.setOutline("red")
    rightEye = leftEye.clone() # rightEye is an exact copy of the left. can't do rightEye = leftEye
    rightEye.move(20,0)
    leftEye.draw(win)
    rightEye.draw(win)
main()