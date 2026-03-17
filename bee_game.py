import pygame

pygame.init()
sc=pygame.display.set_mode((500,500))
pygame.display.set_caption("bee game")
sc.fill("white")
pygame.display.update()

game_over=False
score=0

bee=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/Documents and subjects/python game developer/images/bee.png")

def draw(bee):
    sc.blit(bee,(50,50))
    pygame.display.update()


def movebee(keypress,bee):
    if keypress[pygame.K_LEFT]:
          bee.x=bee.x-1
    if keypress[pygame.K_RIGHT]:
          bee.x=bee.x+1
    if keypress[pygame.K_UP]:
          bee.y=bee.y-1
    if keypress[pygame.K_DOWN]:
          bee.y=bee.y+1
draw(bee)

while True:
    keypress=pygame.key.get_pressed()
    movebee(keypress,bee)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    
