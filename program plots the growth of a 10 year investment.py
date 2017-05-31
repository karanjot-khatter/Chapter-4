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
    print("This program plots the growth of a 10 year investmenent from futval chapter 2")

    #get principal and interest rate from user
    principal = eval(input("Enter the intial principal:"))
    apr = eval(input("Enter the interest rate:"))

    #Create graphics window with labels on left
    win = GraphWin("Investment growth chart", 320,240)  #window size 320 x 240. Called investment growth chart
    win.setBackground("white") #back ground set white - its default grey
    Text(Point(20,230), "0.0K").draw(win) #x = 20 , y =230, 0.0k written and drawn
    Text(Point(20,180), "2.5K").draw(win)
    Text(Point(20,130), "5.0K").draw(win)
    Text(Point(20,80), "7.5K").draw(win)
    Text(Point(20,30), "10.0K").draw(win)

    #Draw bar for intial principal
    height = principal * 0.02
    bar = Rectangle(Point(40,230), Point(65,230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #draw bars for successive years
    for year in range(1,11): #ints 1-10
        #calculate value for next year
        principal = principal * (1-1+apr)
        #draw bar for this value
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11,230), Point(x11+25, 230 - height))
        bar.setFill("green") # represents money - setOutline default black stands out already.
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()