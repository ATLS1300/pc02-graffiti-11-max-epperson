#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Max Epperson
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
home()
showturtle()
up()
clear()
goto(120,-90)
clear()

color(168,204,215) #piss jar base
width(5)
down()
fillcolor(225,225,20)
begin_fill()
left(90)
forward(50)
right(45)
goto(130,-30)
right(45)
forward(100)
right(45)
goto(240,-40)
right(45)
forward(150)
right(45)
goto(230, -200)
right(45)
forward(100)
right(45)
goto(120,-190)
right(45)
forward(100)
end_fill()

up()            #glass details
goto(130, -190)
down()
right(90)
forward(100)
up()
goto(130,-40)
down()
forward(100)

up()            #jar lid base
goto(130,-25)
color("black")
fillcolor("black")
down()
begin_fill()
forward(100)
left(90)
forward(20)
left(90)
forward(100)
left(90)
forward(20)
end_fill()
 
up()           #jar lid lines
goto(135,-6)
color("white")
width(2)
down()
forward(19)
up()
goto(145,-6)
down()
forward(19)
up()
goto(155,-6)
down()
forward(19)
up()
goto(165,-6)
down()
forward(19)
up()
goto(175,-6)
down()
forward(19)
up()
goto(185,-6)
down()
forward(19)
up()
goto(195,-6)
down()
forward(19)
up()
goto(205,-6)
down()
forward(19)
up()
goto(215,-6)
down()
forward(19)
up()
goto(225,-6)
down()
forward(19)

up()           #piss bubbles
goto(150,-70)
color(199,193,22)
down()
dot(20)
up()
goto(170,-90)
dot(10)
goto(150,-100)
dot(5)

up()              #platter
goto(50,-205)
width(5)
color("black")
fillcolor(190,194,203)
down()
begin_fill()
goto(310,-205)
goto(240,-220)
goto(120,-220)
goto(50,-205)
end_fill()


up()                #speech box
goto(65,50)
fillcolor("white")
down()
begin_fill()
goto(105,90)
goto(325,90)
goto(325,200)
goto(105,200)
goto(105,110)
goto(65,50)
end_fill()

up()               #text in speech box
goto(215,155)
down()
style =("Comic Sans",15,"italic")
write("Thank god for my workers!", font=style , align="center")
up()
goto(215,135)
write("They're always keeping me", font=style, align="center")
up()
goto(215,115)
write("refreshed!", font=style, align="center")

up()              #hand under platter
goto(120,-220)
width(3)
color("black")
fillcolor(255,220,177)
down()
begin_fill()
goto(240,-220)
goto(310,-248)
goto(240,-248)
goto(130,-248)
goto(120,-238)
goto(120,-220)
end_fill()
goto(180,-220)
goto(180,-230)
goto(210,-230)
up()
goto(120,-238)
down()
goto(170,-238)
up()
goto(120,-229)
down()
goto(170,-229)

up()             #3D grey box
goto(65,50)
width(5)
fillcolor("grey")
down()
begin_fill()
goto(80,35)
goto(120,75)
goto(340,75)
goto(340,185)
goto(325,200)
goto(325,90)
goto(105,90)
goto(65,50)
end_fill()
up()
goto(120,75)
down()
goto(105,90)
up()
goto(340,75)
down()
goto(325,90)

up()             #person
goto(-290,125)
down()
circle(40)
up()
goto(-250,85)
down()
goto(-250,-25)
goto(-230,35)
goto(-250,85)
goto(-270,35)
goto(-250,-25)
goto(-260,-75)
goto(-280,-125)
goto(-260,-125)
up()
goto(-250,-25)
down()
goto(-242,-65)
up()
goto(-275,130)
down()
goto(-263,132)
up()
goto(-225,130)
down()
goto(-237,132)
up()
goto(-270,110)
down()
goto(-265,115)
goto(-260,110)
goto(-255,115)
goto(-250,110)
goto(-245,115)
goto(-240,110)
goto(-235,115)
goto(-230,110)

up()             #piss dribble
goto(0,48)
color(225,225,20)
down()
goto(0,20)
dot(8)
up()
goto(10,47)
down()
goto(10,25)
dot(7)

hideturtle() #done, the end







