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
    win= GraphWin("5 dices", 500,100)
    win.setCoords(0,0,5,1)

    for i in range(5):
        dice = Rectangle(Point(0.2+i, 0.2), Point(0.8+i, 0.8))
        dice.setFill("red")
        dice.draw(win)

    center = Point(0.5,0.5)
    #dice 1
    d1 = Circle(center,0.05)
    d1.setFill("black")
    d1.draw(win)

    #dice2
    d2 = d1.clone()
    d2.move(0.9, -0.15)
    d2.draw(win)

    d3 = d2.clone()
    d3.move(0.25,0.30)
    d3.draw(win)

    #dice 3

    d4 = d1.clone()
    d4.move(2,0)
    d4.draw(win)

    d5 = d2.clone()
    d5.move(0.95,0)
    d5.draw(win)

    d6 = d3.clone()
    d6.move(1,0)
    d6.draw(win)

    #Dice 4

    d7 = d4.clone()
    d7.move(0.8, 0.2)
    d7.draw(win)

    d8 = d7.clone()
    d8.move(0,-0.4)
    d8.draw(win)

    d9 = d7.clone()
    d9.move(0.4,0)
    d9.draw(win)

    d10 = d9.clone()
    d10.move(0,-0.4)
    d10.draw(win)

    #Dice 5

    d11 = d7.clone()
    d11.move(1, 0)
    d11.draw(win)

    d12 = d8.clone()
    d12.move(1,0)
    d12.draw(win)

    d13 = d9.clone()
    d13.move(1,0)
    d13.draw(win)

    d14 = d10.clone()
    d14.move(1,0)
    d14.draw(win)

    d15 = d4.clone()
    d15.move(2,0)
    d15.draw(win)

    win.getMouse()
    win.close()


main()