#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     29/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def main():
    win = GraphWin("Draw a triangle")
    win.setCoords(0.0,0.0,10.0,10.0)
    message = Text(Point(5, 0.5), "Click on  3 points") #Text provides prompts. A single text object is created and drawn near the beginning of the program.
    message.draw(win)

    #get and draw 3 vertices of traingle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #Use polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3) #polygon class accepts any number of points and creates a polygon by using line segments to connect the points in order.. and connects last point back to first.
    #triangle = 3 sided polygon.. p1,p2,p3 is the 3 points
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    #wait for another click to exit
    message.setText("Click anywhere to quit.") #To change tghe prompt, setText method changes the text displayed.
    win.getMouse()
    win.close()

main()