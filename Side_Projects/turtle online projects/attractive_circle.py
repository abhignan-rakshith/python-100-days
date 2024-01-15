import turtle 

turtle.bgcolor("red")
tim = turtle.Turtle()
tim.ht()
tim.speed("fastest")
for i in range(180):
   tim.forward(100)
   tim.right(30)
   tim.forward(20)
   tim.left(60)
   tim.forward(50)
   tim.right(30)
   tim.penup()
   tim.setposition(0, 0)
   tim.pendown()
   tim.right(2)
turtle.done()   	