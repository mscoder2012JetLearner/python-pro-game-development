import pgzrun

HEIGHT=500
WIDTH=500

class circles():
    def __init__(self,color,radius,pos):
       self.color=color
       self.radius=radius
       self.pos=pos

    def drawcircle(self):
        screen.draw.filled_circle(self.pos,self.radius,self.color)

circle1=circles(("blue"),150,(150,150))
circle2=circles(("red"),50,(50,50))


def draw():
    circle1.drawcircle()
    circle2.drawcircle()

pgzrun.go()