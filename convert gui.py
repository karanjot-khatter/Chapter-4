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
    win = GraphWin("Celcius Converter", 400,300) #window set to 400 x 300 named celcius convertor
    win.setCoords(0.0,0.0,3.0,4.0) #set cpprdomates tp gp from 0,0 in the lower left to 3,4 in the upper right

    #draw the interfact
    Text(Point(1,3), "Celsius Tempeture:").draw(win) #Text written in accordance to win.setCoords of text
    Text(Point(1,1), "Fahrenheit Temperture").draw(win) #Text written in accordance to win.setCoords of text
    input = Entry(Point(2,3),5) #set input box 1 more to the x of where the celcisu temp is. With a width of 5
    input.setText("0.0") #set box to 0.0
    input.draw(win) #make input text
    output = Text(Point(2,1),"") #set outbox where fahrehiet answer is next to the farhiet box. 1 more of the x... display nothing
    output.draw(win) #make outout text
    button = Text(Point(1.5,2.0), "Convert it") # make text in middle of rectangle. Saying convert it
    button.draw(win) # make button text
    Rectangle(Point(1,1.5),Point(2,2.5)).draw(win) #Rectangle representing button

    #wait for a mouse click
    win.getMouse()

    #convert input
    celcius = eval(input.getText())
    fahrenheit = 9.0/5.0 * celcius + 32

    #display output and change button
    output.setText(fahrenheit)
    button.setText("Quit")

    #wait for click and then quit
    win.getMouse()
    win.close()

main()