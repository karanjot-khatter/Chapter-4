#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     06/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import math

def main():
    win= GraphWin("Line segment information",300,420)
    win.setCoords(-10,-14,10,14)
    win.setBackground("white")

    #intro box
    intro = Rectangle(Point(10,14),Point(-10,10))
    intro.setFill("green")
    intro.setWidth(1) #boarder width of box
    intro.draw(win)
    topText1 = Text(Point(0,13),"Click 2 points on map to draw a line").draw(win)
    topText2 = Text(Point(0,11.5),"and length and slope information").draw(win)

    #result box
    result = Rectangle(Point(-10,-14),Point(10,-10)) #opposite intro box
    result.setFill("green")
    result.setWidth(1)
    result.draw(win)
    BottomText = Text(Point(-6,-11.5),"Length:")
    BottomText.setStyle("bold")
    BottomText.draw(win)
    BottomText = Text(Point(-6.5,-12.5),"(in cm)").draw(win)
    inputL = Entry(Point(-2, -11.5),6) #width of 6
    inputL.setText(0)
    inputL.draw(win)
    BottomText = Text(Point(2,-11.5),"Slope:")
    BottomText.setStyle("bold")
    BottomText.draw(win)
    inputS = Entry(Point(6, -11.5),6) #width of 6
    inputS.setText(0)
    inputS.draw(win)

    #grey checkered box
    for i in range(1,20):
        vertical= Line(Point(i-10,-10),Point(i-10,10)) #vertical (x) going from top to bottom.
        vertical.setFill("grey")
        vertical.draw(win)
        horizontal = Line(Point(-10,i-10),Point(10,i-10)) #horizontal (y) going side to side.
        horizontal.setFill("grey")
        horizontal.draw(win)

    #indicator bar
        xAxis = Line(Point(-10,0),Point(10,0))
        yAxis = Line(Point(0,-10),Point(0,10))
        xAxis.setWidth(2)
        yAxis.setWidth(2)
        xAxis.draw(win)
        yAxis.draw(win)

    #Points
    z = q = 1

    for i in range(1,10):
        num = Text(Point(z,-0.5),i) #x axis 2nd half
        num.setSize(5)
        num.draw(win)
        num2 = Text(Point(-z,-0.5),-i) #x axis 1st half
        num2.setSize(5)
        num2.draw(win)
        num3 = Text(Point(-0.5,z),i) #x axis 1st half
        num3.setSize(5)
        num3.draw(win)
        num4 = Text(Point(-0.5,-z),-i) #x axis 1st half
        num4.setSize(5)
        num4.draw(win)

        z = z + 1 #1 each coord - REMEMBER KEEP THIS IN THE LOOP

    # indicator bar **px (0.025 Coord each - 1/8)
    for i in range(-10,10):
        i = i/1 #1 space difference
        Line(Point(-0.2,i),Point(0.2,i)).draw(win) #y small crosses
        Line(Point(i,-0.2),Point(i,0.2)).draw(win) #x small crosses

    p1 = win.getMouse()
    p1.draw(win)
    print(p1)

    p2 = win.getMouse()
    p2.draw(win)
    print(p2)

    line = Line(p1,p2)
    line.setWidth(2)
    line.draw(win)

    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()

    dx = x2 - x1
    dy = y2 - y1
    slope = dy/dx
    slope = round(slope,2)

    inputS.setText(slope)

    length = math.sqrt(dx**2 + dy**2)
    length = round(length,2)

    inputL.setText(length)

    middleX = x2 - (dx/2)
    middleY = y2 -(dy/2)

    middle = Circle(Point(middleX,middleY),0.2) #size of
    middle.setFill('cyan')
    middle.draw(win)

    topText1.setText("")
    topText2.setText("Done click anywhere to quit!")



    win.getMouse()
    win.close()
main()