from turtle import *
c = Turtle()
colormode(255)

def reminder():
  # by Mr. Riley
  # don't forget to put a comment with your name at the top of each function you make
  # this will help to keep track of who created each function
  return True
  
def cloud():
    #by Dalton
    tracer(0)
    c.fillcolor("light grey")
    c.begin_fill()
    c.pencolor("grey")
    for i in range(90):
        c.forward(1*size)
        c.right(1)
    for i in range(180):
        c.forward(1*size)
        c.left(1)
    for i in range(180):
        c.forward(1*size)
        c.right(1)
    for i in range(180):
        c.forward(1*size)
        c.left(1)
    for i in range(175):
        c.forward(1*size)
        c.right(1)
    for i in range(185):
        c.forward(1*size)
        c.left(1)
    for i in range(170):
        c.forward(1*size)
        c.right(1)
    for i in range(190):
        c.forward(1*size)
        c.left(1)
    for i in range(165):
        c.forward(1*size)
        c.right(1)
    for i in range(195):
        c.forward(1*size)
        c.left(1)
    for i in range(160):
        c.forward(1*size)
        c.right(1)
    for i in range(200):
        c.forward(1*size)
        c.left(1)
    for i in range(155):
        c.forward(1*size)
        c.right(1)
    for i in range(205):
        c.forward(1*size)
        c.left(1)
    for i in range(150):
        c.forward(1*size)
        c.right(1)
    for i in range(180):
        c.forward(1*size)
        c.left(1)
    for i in range(180):
        c.forward(1*size)
        c.right(1)
    for i in range(180):
        c.forward(1*size)
        c.left(1)
    for i in range(180):
        c.forward(1*size)
        c.right(1)
    for i in range(180):
        c.forward(1*size)
        c.left(1)
    for i in range(180):
        c.forward(1*size)
        c.right(1)
    for i in range(180):
        c.forward(1*size)
        c.left(1)
    for i in range(175):
        c.forward(1*size)
        c.right(1)
    for i in range(185):
        c.forward(1*size)
        c.left(1)
    for i in range(170):
        c.forward(1*size)
        c.right(1)
    for i in range(190):
        c.forward(1*size)
        c.left(1)
    for i in range(165):
        c.forward(1*size)
        c.right(1)
    for i in range(195):
        c.forward(1*size)
        c.left(1)
    for i in range(160):
        c.forward(1*size)
        c.right(1)
    for i in range(200):
        c.forward(1*size)
        c.left(1)
    for i in range(155):
        c.forward(1*size)
        c.right(1)
    for i in range(205):
        c.forward(1*size)
        c.left(1)
    for i in range(150):
        c.forward(1*size)
        c.right(1)
    for i in range(180):
        c.forward(1*size)
        c.left(1)
    for i in range(180):
        c.forward(1*size)
        c.right(1)
    for i in range(180):
        c.forward(1*size)
        c.left(1)
    for i in range(90):
        c.forward(1*size)
        c.right(1)
    c.end_fill()
    update()

def tree():
    #by Dalton
    c.fillcolor("brown")
    c.begin_fill()
    c.setheading(0)
    for i in range(2):
        c.forward(20)
        c.left(90)
        c.forward(75)
        c.left(90)
    c.end_fill()
    c.left(90)
    c.forward(75)
    c.left(90)
    c.forward(-10)
    c.fillcolor("green")
    c.begin_fill()
    for i in range(90):
        c.forward(1)
        c.right(1)
    c.setheading(270)
    for i in range(180):
        c.forward(1)
        c.left(1)
    for i in range(100):
        c.forward(1.2)
        c.left(.65)
    c.left(55)
    for i in range(100):
        c.forward(1.2)
        c.left(.65)
    for i in range(90):
        c.forward(1)
        c.left(1)
    c.end_fill()
