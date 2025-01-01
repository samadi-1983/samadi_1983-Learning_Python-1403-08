import turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")  


num_lines = 137


for i in range(num_lines):
    t.forward(100)  
    t.backward(100)  
    t.right(2)  


turtle.done()
