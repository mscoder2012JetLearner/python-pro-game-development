import pygame
pygame.init()
sc=pygame.display.set_mode((900,500))
shipWidth=55
shipHeight=40

spaceship1=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/python pro game developer/images/space ship 1.png")
spaceship1=pygame.transform.scale(spaceship1,(shipWidth,shipHeight))

spaceship2=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/python pro game developer/images/space ship 2.png")
spaceship2=pygame.transform.scale(spaceship2,(shipWidth,shipHeight))

background=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/python pro game developer/images/space bg.png")
background=pygame.transform.scale(background,(900,500))

ship1rect=pygame.Rect(225,250,shipWidth,shipHeight)
ship2rect=pygame.Rect(675,250,shipWidth,shipHeight)

def draw(ship1rect,ship2rect):
    sc.blit(background,(0,0))
    rectangle=pygame.Rect(440,0,20,500)
    pygame.draw.rect(sc,"black",rectangle)
    sc.blit(spaceship1,(ship1rect.x,ship1rect.y))
    sc.blit(spaceship2,(ship2rect.x,ship2rect.y))
    pygame.display.update()

    

draw(ship1rect,ship2rect)




while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()