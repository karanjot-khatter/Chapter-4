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
    #Introduction
    print("This program plots the growth of a 10 - year investment") #description

    #get principal and interest rate
    principal = eval(input("Enter the intial principal:")) #input
    apr = eval(input("Enter the interest rate:")) #input

    #Create a graphics windows and labels on side
    win = GraphWin("Investment growth chart", 320, 240) # window created with size and description
    win.setBackground("White") #default colour changed from grey
    win.setCoords(-1.75,-200, 11.5, 10400) # graphics windows go from 0 through to 11.5k, and stop at 10400 this adds space on the graph
    Text(Point(-1,0), "0.0K").draw(win) #Since our bars start at 0, we can locate the left side labelled at -1
    Text(Point(-1,2500), "2.5K").draw(win)
    Text(Point(-1,5000), "5.0K").draw(win)
    Text(Point(-1,7500), "7.5K").draw(win)
    Text(Point(-1,10000), "10.0K").draw(win)

    #draw bar for the intial principal
    bar = Rectangle(Point(0,0), Point(1,principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw a bar for each subsequent year
    for year in range(1,11):
        principal = principal * (1 +apr)
        bar = Rectangle(Point(year,0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

main()