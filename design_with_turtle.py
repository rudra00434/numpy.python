import turtle
import colorsys
tur=turtle.Turtle()
turtle.Screen().bgcolor('black')
tur.speed(0)
n=36
h=0
for i in range(460):
    c=colorsys.hsv_to_rgb(h,1,0.9)
    h=h+1/n
    tur.color(c)
    tur.left(145)
    for i in range(5):
        tur.forward(300)
        tur.left(150)
turtle.done()
