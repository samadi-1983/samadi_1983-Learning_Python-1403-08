import turtle
t = turtle.Turtle()
t.speed(0)  


num_turns = 20
side_length = 10  


for i in range(num_turns):
    t.forward(side_length)
    t.left(45)  
    side_length += 10  

turtle.done()
