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
import math
from graphics import *

def main():
    print("This program computers the intersection of a circle")
    win = GraphWin("Cirlce intersection", 600,300)
    win.setBackground("white")
    win.setCoords(0,0,6,3)
    title = Text(Point(4.5,2.9), "Program to calcuclate X value ") #title
    title.setStyle("bold")
    title.draw(win)

    #chart
    chart = Rectangle(Point(0.25,2.8), Point(2.75,0.25))
    chart.setFill("grey")
    chart.draw(win)

    #intersect at 0,0
    Line(Point(1.5, 0.25), Point(1.5,2.8)).draw(win)
    Line(Point(0.25,1.5),Point(2.75,1.5)).draw(win)

    # indicator bar **px (0.025 Coord each - 1/8)
    for i in range(2,23):
        i = i/8
        Line(Point(0.3,i),Point(0.20,i)).draw(win) #y small crosses
        Line(Point(i,2.825),Point(i,2.75)).draw(win) #x small crosses

    #Number bar
    z = q = 1.5 #start from the top

    for i in range(0,11):
        num = Text(Point(0.10,z),i) #y axis first half
        num.setSize(7)
        num.draw(win)

        num3 = Text(Point(0.10,q),-i) #y axis second half
        num3.setSize(7)
        num3.draw(win)

        num2 = Text(Point(z,2.9),i) #x asis second half
        num2.setSize(7)
        num2.draw(win)

        num4 = Text(Point(q,2.9),-i) #x asis first half
        num4.setSize(7)
        num4.draw(win)

        z = z+0.125 #1/8 - set coordinate eat
        q= q - 0.125 #1/8 - set coordinate each

    Text(Point(4.5,2), "Circle radius (1 to 10): ").draw(win) #Text
    inputR = Entry(Point(4.5, 1.75),6) #width of 6
    inputR.setText(0)
    inputR.draw(win)

    Text(Point(4.5,1.5), "Horizontal line intersection (-10 to 10): ").draw(win) #Text
    inputH = Entry(Point(4.5, 1.25),6) #width of 6
    inputH.setText(0)
    inputH.draw(win)

    Text(Point(4.5,1), "X intersection at:").draw(win) #Text
    Text(Point(4.15,0.75), "+").draw(win) #Text
    Text(Point(4.15,0.70), "-").draw(win) #Text
    answerX = Entry(Point(4.5, 0.75),6) #width of 6
    answerX.setText("?")
    answerX.draw(win)

    Button = Rectangle(Point(3.75, 0.3), Point(5.25,0.5)).draw(win)
    Button.setFill("green")
    Text(Point(4.5,0.4), "click to calculate").draw(win) #Text

    #after user input
    win.getMouse()

    r = eval(inputR.getText())
    h = eval(inputH.getText())


    x = math.sqrt(r**2 - h**2)


    x=round(x,2)

    answerX.setText(x)

    #make circle
    r = r/8 #1 coord - 0.125 unit in map
    resultC = Circle(Point(1.5,1.5),r)
    resultC.setFill("yellow")
    resultC.draw(win)

    #after circle drawn - lines not visible - so redraw
    Line(Point(1.5, 0.25), Point(1.5,2.8)).draw(win)
    Line(Point(0.25,1.5),Point(2.75,1.5)).draw(win)

    #y intersect line
    h = h/8 + 1.5 #1 coord - 0.125
    lineY = Line(Point(0.25,h), Point(2.75,h)) #1 side to another - same height
    lineY.setFill("green")
    lineY.draw(win)

    x = x/ 8 #each coord 0.125
    xA = x+1.5 #start at center move right
    xB = 1.5 - x #start at center move left

    #red dot on answer - first point (+)
    resultA = Circle(Point(xA,h),0.05) #size of
    resultA.setFill('red')
    resultA.draw(win)

    #red dot on answer - second point (-)
    resultB = Circle(Point(xB,h),0.05) #size of
    resultB.setFill('red')
    resultB.draw(win)


    win.getMouse()
    win.close()



main()