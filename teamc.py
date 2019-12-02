from turtle import *
from random import *
tracer(0)
c = Turtle()
colormode(255)

def reminder():
  # by Mr. Riley
  # don't forget to put a comment with your name at the top of each function you make
  # this will help to keep track of who created each function
  return True

def deadTree():
  #by Dalton
    c.fillcolor("brown")
    c.begin_fill()
    c.setheading(0)
    for i in range(2):
        c.forward(25)
        c.left(90)
        c.forward(150)
        c.left(90)
    c.end_fill()
    c.fillcolor("brown")
    c.begin_fill()
    c.left(90)
    c.forward(50)
    c.left(45)
    c.forward(50)
    c.left(90)
    c.forward(10)
    c.left(90)
    c.forward(60)
    c.end_fill()
    c.fillcolor("brown")
    c.begin_fill()
    c.left(135)
    c.forward(115)
    c.right(90)
    c.forward(25)
    c.right(90)
    c.forward(30)
    c.left(120)
    c.forward(40)
    c.right(90)
    c.forward(10)
    c.right(90)
    c.forward(45)
    c.end_fill()
  
def cloud():
    #by Dalton
    c.fillcolor("light grey")
    c.begin_fill()
    c.pencolor("grey")
    size = random()/10 + .1
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
    
def drawOneFish():
    #by Callie
    c.fillcolor(randint(0,255),randint(0,255),randint(0,255)) #random fill color
    c.begin_fill()
    c.left(60)
    number = randint(10,100)
    number = number/100 #divides the number by 100 to make the fish body smaller
    for i in range(120):
        c.forward(number)
        c.right(1)
    c.right(60)
    for i in range(120):
        c.forward(number) #Goes to position to make the tail
        c.right(1)
    c.right(60)
    for i in range(120):
        c.forward(number)
        c.right(1)
    c.forward(30*number) #draws fish tail (makes the tail proportional to the fish body)
    c.left(150)
    c.forward(50*number)
    c.left(150)
    c.forward(30*number)
    c.end_fill()
    c.right(60)

def drawOneSeaweed():
    #by Callie
    c.pencolor("light green")
    c.fillcolor("light green")
    c.begin_fill()
    diameter = randint(10,30) #make a semicircle
    for i in range(randint(3,10)):
        c.circle((diameter/2), 180,)
        c.left(90)
        c.forward(diameter)
        c.forward(-diameter)
        c.right(90)
        c.circle((-diameter/2), 180) #make another semicircle but in the opposite direction so that it does not form a complete circle
        c.right(90)
        c.forward(diameter)
        c.forward(-diameter)
        c.left(90)
        position = c.ycor()
    if position > 295: #stop seaweed if it goes above the waves
        c.penup()
        c.end_fill()
    c.end_fill()

def sunWithRays():
    #by Callie
    c.penup()
    startX = c.xcor()
    startY = c.ycor()
    c.pencolor("yellow")
    c.pensize(10)
    c.fillcolor("yellow")
    c.setheading(90)
    c.forward(50)
    c.setheading(0)
    c.begin_fill()
    c.pendown()
    for i in range(400):
        c.forward(1)
        c.left(1)
    c.end_fill()
    c.penup()
    c.goto(startX, startY-20)
    c.pendown()
    c.right(130)
    c.forward(50)
    c.penup()
    c.goto(startX+150, startY-20)
    c.pendown()
    c.right(140)
    c.forward(50)
    c.penup()
    c.goto(startX+150, startY+100)
    c.pendown()
    c.right(140)
    c.forward(50)
    c.penup()
    c.goto(startX+150, startY+220)
    c.pendown()
    c.right(130)
    c.forward(50)
    c.penup()
    c.goto(startX, startY+250)
    c.pendown()
    c.right(130)
    c.forward(50)
    c.penup()
    c.goto(startX-150, startY+250)
    c.pendown()
    c.right(140)
    c.forward(50)
    c.penup()
    c.goto(startX-150, startY+100)
    c.pendown()
    c.right(140)
    c.forward(50)
    c.penup()
    c.goto(startX-150, startY-20)
    c.pendown()
    c.right(130)
    c.forward(50)

def drawStarFish():
    #by Callie
    c.pendown()
    c.pencolor("pink")
    c.begin_fill()
    c.fillcolor("pink")
    for i in range(5): #draw star shape
        c.forward(40)
        c.right(144)
    c.end_fill()


    
randomColor = (randint(0,255), randint(0,255), randint(0,255)) 
def getRandomColor():
   return  (randint(0,255), randint(0,255), randint(0,255))

tracer(0)
c = Turtle()
def ballon():
 #ByAmrit
 randomColor = getRandomColor()
 c.fillcolor(randomColor)
 c.penup()
 c.goto(0,0)
 c.begin_fill()
 c.pendown()
for i in range(360):
  c.forward(1)
  c.right(1)
c.penup()
c.goto(0,-110)
c.setheading(270)
c.pendown()
c.forward(200)

ballon()
 

def drawTriangle():
  for i in range(3):
    c.forward(45)
    c.right(120)
c.penup()
c.goto(0,-117)
drawTriangle()

    
def drawRainbowStripe(number1, number2):
    #by Callie
    c.pendown()
    c.forward(10)
    c.setheading(90)
    for i in range(180):
        c.forward(1/number1)
        c.right(1)
    c.setheading(0)
    c.forward(10)
    c.setheading(90)
    for i in range(183):
        c.forward(1.17/number2)
        c.left(1)

def redStripe():
    #by Callie
    c.begin_fill()
    c.fillcolor("red")
    drawRainbowStripe(1, 1)
    c.end_fill()
    c.setheading(0)
    c.forward(5)

def orangeStripe():
    #by Callie
    c.begin_fill()
    c.fillcolor("orange")
    drawRainbowStripe(1.11, 1.1)
    c.end_fill()
    c.setheading(0)
    c.forward(5)

def yellowStripe():
    #by Callie
    c.begin_fill()
    c.fillcolor("yellow")
    drawRainbowStripe(1.25, 1.2)
    c.end_fill()
    c.setheading(0)
    c.forward(5)

def greenStripe():
    #by Callie
    c.begin_fill()
    c.fillcolor("green")
    drawRainbowStripe(1.5, 1.4)
    c.end_fill()
    c.setheading(0)
    c.forward(5)

def blueStripe():
    #by Callie
    c.begin_fill()
    c.fillcolor("blue")
    drawRainbowStripe(1.7, 1.55)
    c.end_fill()
    c.setheading(0)
    c.forward(5)

def purpleStripe():
    #by Callie
    c.begin_fill()
    c.fillcolor("purple")
    drawRainbowStripe(2, 1.8)
    c.end_fill()

def drawRainbow():
    #by Callie
    redStripe()
    orangeStripe()
    yellowStripe()
    greenStripe()
    blueStripe()
    purpleStripe()

def drawRect(topLeftX, topLeftY, width, height, color):
  #by Callie
    c.penup()
    c.goto(topLeftX, topLeftY)
    c.setheading(0)
    c.fillcolor(color)
    c.begin_fill()
    c.pendown()
    for i in range(2):
        c.forward(width)
        c.right(90)
        c.forward(height)
        c.right(90)
    c.end_fill()
 
def drawCircle(centerX , centerY , radius , color):
    #by Jon
    #radius must be 58+ to make complete circle
    circle = 2 * pi * radius / 360
    c.penup()
    c.goto(centerX , centerY)
    c.setheading(0)
    c.forward(radius)
    c.right(90)
    c.fillcolor(color)
    c.begin_fill()
    c.pendown()
    for i in range(360):
        c.forward(circle)
        c.right(circle)
    c.end_fill()
    
def drawFence():
    #by jon
    for i in range(10):
        c.forward(10)
        c.left(90)
        c.forward(50)
        c.left(45)
        c.forward(7)
        c.left(90)
        c.forward(7)
        c.left(45)
        c.forward(50)
        c.left(90)
        c.forward(10)    
        
def drawSandcastle2():
    c.fillcolor(181,101,29)
    c.begin_fill()
    c.forward(70)
    c.left(90)
    c.forward(40)
    for i in range(3):
        c.forward(10)
        c.left(90)
        c.forward(10)
        c.left(90)
        c.forward(10)
        c.right(90)
        c.forward(10)
        c.right(90)
    c.forward(10)
    c.left(90)
    c.forward(10)
    c.left(90)
    c.forward(50)
    c.penup()
    c.setheading(0)
    c.forward(60)
    c.left(90)
    c.forward(40)
    c.pendown()
    c.setheading(90)
    c.forward(20)
    for i in range(2):
        c.forward(10)
        c.left(90)
        c.forward(10)
        c.left(90)
        c.forward(10)
        c.right(90)
        c.forward(10)
        c.right(90)
    c.forward(10)
    c.left(90)
    c.forward(10)
    c.left(90)
    c.forward(30)
    c.penup()
    c.left(90)
    c.forward(40)
    c.left(90)
    c.forward(20)
    c.setheading(90)
    c.pendown()
    c.forward(20)
    for i in range(1):
        c.forward(10)
        c.left(90)
        c.forward(10)
        c.left(90)
        c.forward(10)
        c.right(90)
        c.forward(10)
        c.right(90)
    c.forward(10)
    c.left(90)
    c.forward(10)
    c.left(90)
    c.forward(20)
    c.end_fill()
    c.penup()
    c.left(180)
    c.forward(10)
    c.right(90)
    c.forward(13)
    #flag start
    c.penup()
    c.goto(33,80)
    c.setheading(90)
    c.fillcolor("black")
    c.begin_fill()
    c.pendown()
    c.forward(40)
    c.right(90)
    c.forward(4)
    c.right(90)
    c.forward(40)
    c.right(90)
    c.forward(4)
    c.end_fill()
    #triangle
    c.penup()
    c.goto(38,120)
    c.setheading(90)
    c.pendown()
    c.fillcolor("red")
    c.begin_fill()
    c.right(135)
    c.forward(20)
    c.right(90)
    c.forward(20)
    c.end_fill()
    c.penup()
    c.setheading(270)
    c.forward(91.71572875253811)
    c.right(90)
    c.forward(19.5)
    c.setheading(90)
    c.pendown()
    for i in range(180):
        c.forward(.3)
        c.right(1)
   
def kite():
    #by jon
    c.pendown()
    c.left(45)
    c.forward(100)
    c.right(90)
    c.forward(100)
    c.right(90)
    c.forward(100)
    c.right(90)
    c.forward(100)
    c.right(135)
    c.forward(140)
    c.left(180)
    c.forward(70)
    c.right(90)
    c.forward(70)
    c.right(180)
    c.forward(250)
    
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
cloud()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
tree()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
drawOneFish()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
drawOneSeaweed()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
sunWithRays()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
drawStarFish()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
drawRainbow()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
drawRect()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
drawCircle()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
drawFence()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
drawSandcastle()
c.penup()
c.goto(randint(-450, 450), randint(-450, 450))
kite()


update()
