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
    c.pencolor("yellow")
    c.pensize(10)
    c.fillcolor("yellow")
    c.begin_fill()
    c.pendown()
    for i in range(400):
        c.forward(2)
        c.left(1)
    c.end_fill()
    c.penup()
    c.goto(0, -20)
    c.pendown()
    c.right(130)
    c.forward(50)
    c.penup()
    c.goto(150, -20)
    c.pendown()
    c.right(140)
    c.forward(50)
    c.penup()
    c.goto(150, 100)
    c.pendown()
    c.right(140)
    c.forward(50)
    c.penup()
    c.goto(150, 220)
    c.pendown()
    c.right(130)
    c.forward(50)
    c.penup()
    c.goto(0, 250)
    c.pendown()
    c.right(130)
    c.forward(50)
    c.penup()
    c.goto(-150, 250)
    c.pendown()
    c.right(140)
    c.forward(50)
    c.penup()
    c.goto(-150, 100)
    c.pendown()
    c.right(140)
    c.forward(50)
    c.penup()
    c.goto(-150, -20)
    c.pendown()
    c.right(130)
    c.forward(50)

def drawStarFish():
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
 #Amrit
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

update()
