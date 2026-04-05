#by Arshia 
import turtle
turtle.color("red")
turtle.pensize(5)
def polygon(num,size):
    for i in range(num):
        turtle.forward(size)
        turtle.left(360/num)
def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()
polygon(5,50)
back(125)
polygon(4,50)
