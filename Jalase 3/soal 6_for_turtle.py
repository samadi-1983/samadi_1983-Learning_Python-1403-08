import turtle
t = turtle.Turtle()
t.speed(0)  


num_squares = 20
step = 15


for i in range(num_squares):
    for f in range(4):
        t.forward(step)
        t.left(90)
      
    step += 15

turtle.done()
