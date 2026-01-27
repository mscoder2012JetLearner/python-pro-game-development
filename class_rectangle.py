import pygame
pygame.init()

sc=pygame.display.set_mode((500,500))
pygame.display.set_caption("Output")
sc.fill("black")
pygame.display.update()

class rectangle():
    
    def __init__(self,color,dimension):
        self.color=color
        self.dimension=dimension

    def draw(self):
        pygame.draw.rect(sc,self.color,self.dimension,10)

rectangle1=rectangle("blue",(150,150,150,150))
rectangle1.draw()
rectangle2=rectangle("red",(50,50,50,50))
rectangle2.draw()
pygame.display.update()

        
    

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()

