#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     07/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import math
def main():

    win= GraphWin("Line segment information",600,300)
    win.setCoords(0,0,6,3)
    win.setBackground("white")

    #intro text
    topText = Text(Point(4.5,2.6),"Click inside the left field to")
    topText.setStyle("bold")
    topText.draw(win)
    topText = Text(Point(4.5,2.4),"draw a rectangle and to")
    topText.setStyle("bold")
    topText.draw(win)
    topText = Text(Point(4.5,2.2),"recieve the area and perimeter")
    topText.setStyle("bold")
    topText.draw(win)
    topText = Text(Point(4.5,2.0),"information below")
    topText.setStyle("bold")
    topText.draw(win)

    areaText = Text(Point(4.2,1.5),"Area: (cm^2)").draw(win)
    areaBox = Entry(Point(5,1.5),6)
    areaBox.setText("0")
    areaBox.draw(win)

    areaText = Text(Point(4,1.25),"Perimeter: (cm)").draw(win)
    perimeterBox = Entry(Point(5,1.25),6)
    perimeterBox.setText("0")
    perimeterBox.draw(win)

    button = Rectangle(Point(3.5,0.75),Point(5.5,0.25))
    button.setFill("green")
    button.draw(win)

    buttonText1 = Text(Point(4.5,0.6),"Tap two points to get ")
    buttonText1.setStyle("bold")
    buttonText1.draw(win)
    buttonText2 = Text(Point(4.5,0.4),"the information above ")
    buttonText2.setStyle("bold")
    buttonText2.draw(win)

        #grey checkered box
    for i in range(2,23):
        vertical= Line(Point(i/8,0.5),Point(i/8,2.5)) #vertical (x) going from top to bottom.
        vertical.setFill("grey")
        vertical.draw(win)
        horizontal = Line(Point(0.5,i/8),Point(2.5,i/8)) #horizontal (y) going side to side.
        horizontal.setFill("grey")
        horizontal.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    print(p1)

    p2 = win.getMouse()
    p2.draw(win)
    print(p2)

    p3 = win.getMouse()
    p3.draw(win)
    print(p3)

    triangleDraw = Polygon(p1,p2,p3)
    triangleDraw.setFill("white")
    triangleDraw.draw(win)

    x1 = p1.getX() * 8 #times by 8 - cos coordinates are divided above
    y1 = p1.getY() * 8
    x2 = p2.getX() * 8
    y2 = p2.getY() * 8
    x3 = p3.getX() * 8
    y3 = p3.getY() * 8

    #width and length
    dx =  x1 - x2
    dy =  y1 - y2
    a = math.sqrt(dx**2 + dy**2)

    dx = x2 - x3
    dy = y2 - y3
    b = math.sqrt(dx**2 + dy **2)

    dx = x3 - x1
    dy = y3 - y1
    c = math.sqrt(dx**2 + dy **2)


    #formulae of area and perimeter
    s =(a+b+c) / 2
    area = math.sqrt(s*(s-a) * (s-b) * (s-c))
    perimeter = a + b + c

    areaBox.setText(round(area,2))
    perimeterBox.setText(round(perimeter,2))

    buttonText2.setText("")
    buttonText2.setText("Close")


    win.getMouse()
    win.close()
main()