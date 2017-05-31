#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     01/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def main():
    win = GraphWin("Program draws a face", 300, 300)
    center = Point(150,150)

    face = Circle(center,100) #furtherest away - later objects will appear ontop of earlier
    face.setFill("white")
    face.draw(win)

    lEyebrow = Line(Point(100, 110), Point(150,110))
    lEyebrow.setFill("black")
    lEyebrow.setWidth(10)
    rEyebrow = Line(Point(160, 110), Point(210,110))
    rEyebrow.setWidth(10)
    lEyebrow.draw(win)
    rEyebrow.draw(win)

    leftEye = Circle(Point(125,140), 20)
    leftEye.setFill("white")
    leftEye.setOutline("black")
    rightEye = leftEye.clone() # rightEye is an exact copy of the left. can't do rightEye = leftEye
    rightEye.move(60,0)
    leftEye.draw(win)
    rightEye.draw(win)

    lPupil = Circle(Point(125,140), 10)
    lPupil.setFill("black")
    rPupil = lPupil.clone()
    rPupil.move(60,0)
    lPupil.draw(win)
    rPupil.draw(win)

    nose1 = Line(Point(155,150), Point(145,190))
    nose1.draw(win)
    nose2 = Line(Point(145,190), Point(160,190))
    nose2.draw(win)

    mouth = Oval(Point(125, 200), Point(180,230))
    mouth.setOutline("red")
    mouth.draw(win)


    win.getMouse() #when clicked
    win.close() #close program
main()