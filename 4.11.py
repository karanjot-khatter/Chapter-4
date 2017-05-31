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

def main():
    win = GraphWin("Five click house", 500, 350)
    win.setCoords (0,0,10,14)
    win.setBackground("white")

    #intro text
    title = Text(Point(2,13),"Five click house")
    title.setFill("grey")
    title.draw(win)

    #bottom box
    bottomBox = Rectangle(Point(0,0), Point(10,4))
    bottomBox.setFill("green")
    bottomBox.setWidth(2)
    bottomBox.draw(win)

    #bottom box text
    bottomText = Text(Point(2,3),"House builder says:")
    bottomText.setStyle("italic")
    bottomText.draw(win)

    #action Text
    actionText = Text(Point(5,2),"Firstly,Click to locate the houses bottom left corner")
    actionText.setStyle("bold")
    actionText.draw(win)

    #draw bottom left corner
    lCorner = win.getMouse()
    lCorner.draw(win)

    #change action text
    actionText.setText("Secondly, click to locate the houses top right corner")

     #draw top right corner
    rCorner = win.getMouse()
    rCorner.draw(win)

    rectangleFrame = Rectangle(lCorner,rCorner).draw(win)

    #change action text 3

    actionText.setText("Thirdly, click on the the top edge of a rectangle door ")

    #draw top edge of rectangle door
    tEdge = win.getMouse()
    rectangleFrameWidth = rCorner.getX() - lCorner.getX() #door width
    rectangleFrameWidth = abs(rectangleFrameWidth) / 5 #whole number number before divison - door have 1/5 of rectangle frame
    tEdgeLeftSide = tEdge.getX() - rectangleFrameWidth/2 #left side of the line
    tEdgeRightSide = tEdge.getX() + rectangleFrameWidth/2 #right side of the line
    tEdgeTopHeight = tEdge.getY() #click height
    tEdgeBottomHeight = lCorner.getY() #height from bottom click

    rectangleDoor = Rectangle(Point(tEdgeLeftSide,tEdgeTopHeight),Point(tEdgeRightSide,tEdgeBottomHeight)).draw(win)

    #change action text 4
    actionText.setText("Fourthly, this click will indicatge the center of a square window ")
    window = win.getMouse()
    windowFrameWidth = rectangleFrameWidth/2
    leftOfWindow = window.getX() + windowFrameWidth /2
    rightOfWindow = window.getX() - windowFrameWidth/2
    topOfWindow = window.getY() + windowFrameWidth/2
    bottomtOfWindow = window.getY() - windowFrameWidth / 2

    windowDoor = Rectangle(Point(leftOfWindow,topOfWindow), Point(rightOfWindow,bottomtOfWindow)).draw(win)

    #change action 5
    actionText.setText("Lastly, this click will indicate the peak of the roof ")
    roof = win.getMouse()
    #find top left of house
    heightOfHouse = rCorner.getY() - lCorner.getY()
    heightOfHouse = abs(heightOfHouse)
    topLeft = Point(lCorner.getX(), lCorner.getY() + heightOfHouse)

   #draw roof
    roofLeft = Line(roof,topLeft).draw(win)
    roofRight = Line(roof, rCorner).draw(win)

    #completion
    actionText.setText("Done! Click anywhere to exit ")
    bottomBox.setFill("Yellow")

    win.getMouse()
    win.close()
main()