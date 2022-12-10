import turtle
turtle = turtle.Turtle()
turtle.color("black", "#d77803")

turtle.begin_fill()
for i in range(20):
	turtle.forward(110)
	turtle.left(85)
	turtle.dot(20, "#ffda01")
turtle.end_fill()
turtle.penup()
turtle.forward(60)
turtle.setx(8)
turtle.sety(70)

turtle.pendown()
turtle.color("black", "#58351a")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.penup()


turtle.setx(27)
turtle.sety(67)

turtle.pendown()

turtle.color("black", "#361103")
turtle.begin_fill()
turtle.circle(32)
turtle.end_fill()

turtle.setx(27)
turtle.sety(70)
for i in range(80):
	turtle.dot(1, "#ffda01")
	turtle.forward(3)
	turtle.left(5)

turtle.setx(23)
turtle.sety(45)
for i in range(90):
	turtle.dot(1, "#ffda01")
	turtle.forward(5)
	turtle.left(7)
turtle.penup()

turtle.setx(72)
turtle.sety(80)
for i in range(20):
	turtle.dot(1, "#fe7d00")
	turtle.forward(3)
	turtle.left(20)
  
turtle.penup()
turtle.setx(42)
turtle.sety(80)
for i in range(20):
	turtle.dot(1, "#fe7d00")
	turtle.forward(3)
	turtle.left(20)
  
  
turtle.sety(50)
turtle.pendown()
turtle.color("#5b1101", "#ffda01")
turtle.begin_fill()
turtle.circle(15,180)
turtle.penup()
turtle.end_fill()

turtle.pencolor("#black")
turtle.sety(-38)
turtle.setheading (-83)
turtle.pendown()
turtle.fd (90)
turtle.left (90)
turtle.fd (25)
turtle.left (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (-80,90)
turtle.right (90)
turtle.circle (-80,90)
turtle.end_fill ()
turtle.right (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (85)
turtle.left (90)
turtle.fd (80)
  
  

turtle.right (90)
turtle.right (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (80,90)
turtle.left (90)
turtle.circle (80,90)
turtle.end_fill ()
turtle.left (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (60)
turtle.right (90)
turtle.circle (200,60)



turtle.done()
