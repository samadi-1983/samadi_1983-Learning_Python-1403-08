import turtle
t = turtle.Turtle()
t.speed(0)  


num_repeats = 20
step = 10


for i in range(num_repeats):
    t.forward(step)
    t.left(90)
    step += 10  


turtle.done()
