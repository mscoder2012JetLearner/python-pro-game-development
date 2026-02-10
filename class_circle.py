import pgzrun

HEIGHT=500
WIDTH=500
gravity=2000

class circles():
    def __init__(self,color,radius,x,y):
       self.color=color
       self.radius=radius
       self.pos=(x,y)
       self.x=x
       self.y=y
       self.vx=200
       self.vy=0

    def drawcircle(self):
        screen.draw.filled_circle(self.pos,self.radius,self.color)


circle2=circles(("red"),50,50,50)

def draw():
    screen.clear()
    circle2.drawcircle()
    

def update(dt):
    uy=circle2.vy
    circle2.vy=circle2.vy+gravity*dt
    circle2.y=circle2.y+(uy+circle2.vy)*0.5*dt
    print(circle2.y)

pgzrun.go()