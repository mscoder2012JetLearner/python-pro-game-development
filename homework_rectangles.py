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

rectangle1=rectangle("green",(10,150,250,150))
rectangle2=rectangle("purple",(200,230,350,250))
pygame.display.update()

        


while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        elif i.type==pygame.MOUSEBUTTONDOWN:
            rectangle1.draw()
            rectangle2.draw()
            pygame.display.update()
