import pygame

framespersecond=700
clock=pygame.time.Clock()
pygame.init()
sc=pygame.display.set_mode((500,500))
pygame.display.set_caption("bee game")
pygame.display.update()

game_over=False
score=0

bee=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/Documents and subjects/python game developer/images/bee.png")

bee_rect=pygame.Rect(50,50,50,50)

def draw(bee):
    sc.fill("white")
    sc.blit(bee,(bee_rect.x,bee_rect.y))
    pygame.display.update()


def movebee(keypress,bee_rect):
    if keypress[pygame.K_LEFT]:
          bee_rect.x=bee_rect.x-1
    if keypress[pygame.K_RIGHT]:
          bee_rect.x=bee_rect.x+1
    if keypress[pygame.K_UP]:
          bee_rect.y=bee_rect.y-1
    if keypress[pygame.K_DOWN]:
          bee_rect.y=bee_rect.y+1
draw(bee)

while True:
    clock.tick(framespersecond)
    keypress=pygame.key.get_pressed()
    movebee(keypress,bee_rect)
    draw(bee)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    
