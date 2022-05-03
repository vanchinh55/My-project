import turtle
sc = turtle.Screen()
sc.bgcolor("pink")
hv = turtle.Turtle()
hv = turtle.fillcolor("Orange")
hv = turtle.shape("turtle")
for i in range(4):
    hv = turtle.forward(100)
    hv = turtle.left(90)
"""for i in range(0,110,1):
    hv = turtle.forward(5)
    hv = turtle.left(3.14)"""
print(hv)
