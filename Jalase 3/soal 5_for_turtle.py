import turtle
t = turtle.Turtle()
t.speed(0)  
t.color("red")  

number_line=45


for i in range(number_line):
    t.fd(100)
    t.bk(100)
    t.lt(2)
    for h in range(number_line):
         t.fd(100)
         t.bk(100)
         t.right(2)
    
    

turtle.done()
