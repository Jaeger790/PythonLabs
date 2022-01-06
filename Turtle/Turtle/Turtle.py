

    
import turtle

window = turtle.Screen()
window.bgcolor('green')

john = turtle.Turtle()
john.shape('turtle')
john.color('blue')
john.penup()

for i in range(12):
    john.forward(50)
    john.shape('arrow')
    john.pendown()
    john.forward(10)
    john.penup()
    john.forward(20)
    john.shape('turtle')
    john.stamp()
    john.penup()
    john.right(180)
    john.forward(80)
    john.right(180 +30)
    