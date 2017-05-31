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
#Could of used polygon for3 sides instead of lines
def main():
    win = GraphWin("Winter scene", 300, 300)
#stump
    stump = Rectangle(Point(110,180), Point(130,150))
    stump.setFill("black")
    stump.draw(win)

#straight line above stump

    line1 = Line(Point(90,150), Point(150,150))
    line1.setFill("green")
    line1.draw(win)
    line4 = line1.clone()

#diaganal line left
    line2 = Line(Point(90, 150), Point(120, 130))
    line2.setFill("green")
    line2.draw(win)
    line3 = line2.clone()
    line3.move(0,-20)
    line3.draw(win)
    line5 = line3.clone()
    line5.move(0,-20)
    line5.draw(win)


#half line left
    line4 = Line(Point(90,130), Point(120,130))
    line4.setFill("green")
    line4.draw(win)
    line6 = line4.clone()
    line6.move(0,-20)
    line6.draw(win)

#diangoal line right

    line7 = Line(Point(155, 150), Point(125, 130))
    line7.setFill("green")
    line7.draw(win)
    line8 = line7.clone()
    line8.move(0,-20)
    line8.draw(win)
    line9 = line8.clone()
    line9.move(0,-20)
    line9.draw(win)

#half line right
    line10 = Line(Point(155,130), Point(125,130))
    line10.setFill("green")
    line10.draw(win)
    line11 = line10.clone()
    line11.move(0,-20)
    line11.draw(win)

#top

    top = Circle(Point(125,90),5)
    top.setFill("gold")
    top.draw(win)

#snowman

    bottomLayer = Circle(Point(220,220),50)
    bottomLayer.setFill("white")
    bottomLayer.draw(win)

    button4 = Circle(Point(220,220), 5)
    button4.setFill("black")
    button4.draw(win)

    button5 = Circle(Point(220,240), 5)
    button5.setFill("black")
    button5.draw(win)

    button6= Circle(Point(220,200), 5)
    button6.setFill("black")
    button6.draw(win)

    midLayer = Circle(Point(220,130),40)
    midLayer.setFill("white")
    midLayer.draw(win)

    midArmDiagL = Line(Point(260,130), Point(300,90))
    midArmDiagL.setFill("black")
    midArmDiagL.draw(win)

    midArmDiagR = Line(Point(180,130), Point(140,90))
    midArmDiagR.setFill("black")
    midArmDiagR.draw(win)

    button1 = Circle(Point(220,130), 5)
    button1.setFill("black")
    button1.draw(win)

    button2 = Circle(Point(220,150), 5)
    button2.setFill("black")
    button2.draw(win)

    button3= Circle(Point(220,110), 5)
    button3.setFill("black")
    button3.draw(win)

    topLayer = Circle(Point(220,70),25)
    topLayer.setFill("white")
    topLayer.draw(win)

    eyes = Circle(Point(210,65),5)
    eyes.setFill("black")
    Reyes = eyes.clone()
    Reyes.move(20,0)
    eyes.draw(win)
    Reyes.draw(win)

    nose = Polygon(Point(220,70),Point(210,80),Point(230,80))
    nose.setFill("orange")
    nose.draw(win)


    smile = Circle(Point(220,90), 2)
    smile.setFill("Black")
    smile.draw(win)
    smile2 = smile.clone()
    smile2.move(7,0)
    smile2.draw(win)
    smile3 = smile.clone()
    smile3.move(-7,0)
    smile3.draw(win)
    smile4 = Circle(Point(207,85), 2)
    smile4.setFill("Black")
    smile4.draw(win)
    smile5 = smile4.clone()
    smile5.move(25,0)
    smile5.draw(win)

    win.getMouse()
    win.close()

main()