# run in http://python.codeaha.com

sprite = codeaha.Square(-40, 225, 10,"#c8ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-30, 225, 10, "#a6ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-20, 225, 10, "#a6ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-10, 225, 10, "#a6ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(0, 225, 10,"#c8ffff")

# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-40, 215, 10, "#a6ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-30, 215, 10, "#8effff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-20, 215, 10, "#8effff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-10, 215, 10, "#8effff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(0, 215, 10, "#a6ffff")

# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-40, 205, 10, "#8effff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-30, 205, 10, "white")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-20, 205, 10, "#8effff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-10, 205, 10, "white")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-0, 205, 10, "#8effff")

# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-40, 195, 10, "#8effff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-30, 195, 10, "white")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-20, 195, 10, "#8effff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-10, 195, 10, "white")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-0, 195, 10, "#8effff")

# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-40, 185, 10,"#c8ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-30, 185, 10, "#a6ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-20, 185, 10, "#a6ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(-10, 185, 10, "#a6ffff")
# sprite = codeaha.Square(x, y, width, "color")
sprite = codeaha.Square(0, 185, 10,"#c8ffff")

t = turtle.Pen()
t.hideturtle()
# sprite = codeaha.Star(x, y, points, radius, "color")
sprite = codeaha.Star(0, 0, 5, 30, "red")
t.pendown()
stage.set_background("bg_pinkbg02")
#2 floor

# roofy
t.setposition(0, 160)
t.setheading(-90)
width=200
color='red'
for i in range(100):
    t.forward(1)
    t.color(color)
    t.width(width)
    width = width + 2
    if i % 5 == 0:
        t.color('green')
# bodyy of housie
t.color('blue')
t.width(300)
t.forward(130)
# basy of housie
t.color('orange')
t.width(300)
t.forward(10)
# windowy of housie
t.setposition(0,25)
t.color('white')
t.width(250)
t.forward(75)

t.color('blue')
t.width(170)
t.back(75)

t.color('white')
t.width(160)
t.forward(75)

t.color('blue')
t.width(75)
t.back(75)

t.setposition(0,-35)
t.color('blue')
t.width(250)
t.forward(6)

#1 floor
t.setposition(0,-80)
# bodyy of housie
t.color('blue')
t.width(300)
t.forward(130)
# basy of housie
t.color('orange')
t.width(300)
t.forward(10)
# windowy of housie
t.setposition(0,-120)
t.color('white')
t.width(250)
t.forward(75)

t.color('blue')
t.width(170)
t.back(75)

t.color('white')
t.width(160)
t.forward(75)

t.color('blue')
t.width(75)
t.back(75)

t.setposition(0,-155)
t.color('blue')
t.width(250)
t.forward(6)

# doory framy
t.setposition(0,-105)
t.width(40)
t.color('red')
t.forward(110)
#doory
t.width(35)
t.color('darkred')
t.back(80)

t.setposition(0,-130)
t.color('grey')
t.back(20)

# stairy
t.setposition(0,-215)
t.color('purple')
t.width(50)
t.forward(10)
t.color('black')
t.forward(2)
t.width(75)
t.color('purple')
t.forward(10)
t.color('black')
t.forward(2)
t.width(100)
t.color('purple')
t.forward(10)
t.color('black')
t.forward(2)
