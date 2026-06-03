print()
print("Задание №1")
print()

import random
print("Ваше рандомное число:", random.randint(1, 100))

print()
print("Задание №2")
print()

import turtle as t

t.shape("classic")
t.color("red")
t.turtlesize(2, 3, 5)
t.forward(50)
t.speed(100)

size = 200

for i in range(36):
    t.circle(100)
    t.right(10)
    colors = ["red", "orange","yellow","green","blue","indigo","violet"]
    t.pencolor(colors[i % len(colors)])
    
    
t.penup()
t.left(180)
t.forward(250)
t.left(90)
t.forward(125)
t.right(180)
t.pendown()

for i in range(16):
    
    t.forward(62.5)
    t.right(75)
    t.right(112.5)
    
    t.forward(125)
    t.right(150)
    t.right(225)
    colors = ["red", "orange","yellow","green","blue","indigo","violet"]
    t.pencolor(colors[i % len(colors)])
    
t.penup()
t.forward(350)
t.pendown()

for i in range(16):
    
    t.forward(62.5)
    t.right(75)
    t.right(112.5)
    
    t.forward(125)
    t.right(150)
    t.right(225)
    colors = ["red", "orange","yellow","green","blue","indigo","violet"]
    t.pencolor(colors[i % len(colors)])
    
t.penup()
t.right(90)
t.forward(500)
t.pendown()
    
for i in range(16):
    
    t.forward(62.5)
    t.right(75)
    t.right(112.5)
    
    t.forward(125)
    t.right(150)
    t.right(225)
    colors = ["red", "orange","yellow","green","blue","indigo","violet"]
    t.pencolor(colors[i % len(colors)])
    
t.penup()
t.right(90)
t.forward(450)
t.pendown()

for i in range(16):
    
    t.forward(62.5)
    t.right(75)
    t.right(112.5)
    
    t.forward(125)
    t.right(150)
    t.right(225)
    colors = ["red", "orange","yellow","green","blue","indigo","violet"]
    t.pencolor(colors[i % len(colors)])
    
t.penup()
t.right(90)
t.forward(600)
t.right(90)
t.forward(225)
t.pendown()

for i in range(6):
    t.forward(125)
    t.right(75)
    t.right(225)
    colors = ["red", "orange","yellow","green","blue","indigo","violet"]
    t.pencolor(colors[i % len(colors)])
    
t.penup()
t.right(90)
t.forward(750)
t.right(90)
t.forward(25)
t.right(180)
t.pendown()

for i in range(6):
    t.forward(125)
    t.left(75)
    t.left(225)
    colors = ["red", "orange","yellow","green","blue","indigo","violet"]
    t.pencolor(colors[i % len(colors)])
    
t.done()
