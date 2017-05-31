#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     02/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def main():
    #Introduction
    print("This program plots the growth of a 10 - year investment") #description
    win = GraphWin("Investment growth chart", 320, 240) # window created with size and description
    win.setBackground("White") #default colour changed from grey
    win.setCoords(-1.75,-200, 11.5, 10400) # graphics windows go from 0 through to 11.5k, and stop at 10400 this adds space on the graph
    Text(Point(4.5,9000),"Future value calculator").draw(win) #Title displayed in graphic

    #input principal
    Text(Point(4.5,5000),"Input initial principal:").draw(win)
    inputP = Entry(Point(9, 5000),6) #width of 6
    inputP.setText(0)
    inputP.draw(win)

    #input interest
    Text(Point(4.6,3500),"Input initial interest:").draw(win)
    inputI = Entry(Point(9, 3500),6) #width of 6
    inputI.setText(0.0)
    inputI.draw(win)

    #button and wait for mouse click

    button = Rectangle(Point(1, 1500), Point(5,2500))
    button.setFill("green")
    button.draw(win)
    buttonText = Text(Point(3,2000), "Show result")
    buttonText.draw(win)
    win.getMouse()

    #input from user
    principal = eval(inputP.getText())
    interest = eval(inputI.getText())

    #Create a graphics windows and labels on side

    Text(Point(-1,2500), "2.5K").draw(win)
    Text(Point(-1,5000), "5.0K").draw(win)
    Text(Point(-1,7500), "7.5K").draw(win)
    Text(Point(-1,10000), "10.0K").draw(win)

    #draw bar for the intial principal
    bar = Rectangle(Point(0,0), Point(1,principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

  #  Draw a bar for each subsequent year
    for year in range(1,11):
        principal = principal * (1 + interest)
        bar = Rectangle(Point(year,0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    buttonText.setText('Quit.')
    win.getMouse()
    win.close()

main()