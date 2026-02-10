import pgzrun

HEIGHT=500
WIDTH=500
gravity=2000
import os
os.environ['SDL_VIDEO_CENTERED']='1'

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
        self.pos=(self.x,self.y)
        screen.draw.filled_circle(self.pos,self.radius,self.color)


circle2=circles(("red"),50,50,50)

def draw():
    screen.clear()
    circle2.drawcircle()
    

def update(dt):
    uy=circle2.vy
    circle2.vy=circle2.vy+gravity*dt
    circle2.y=circle2.y+(uy+circle2.vy)*0.5*dt
    if circle2.y>500:
        circle2.y=500-circle2.radius
        circle2.vy=-circle2.vy*0.9
    circle2.x=circle2.x+circle2.vx*dt
    if circle2.x>500 or circle2.x<0:
        circle2.vx=-circle2.vx*0.9
        


pgzrun.go()