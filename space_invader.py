import pygame
pygame.font.init()
pygame.init()
sc=pygame.display.set_mode((900,500))
shipWidth=55
shipHeight=40
ship1health=10
ship2health=10

spaceship1=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/python pro game developer/images/space ship 1.png")
spaceship1=pygame.transform.scale(spaceship1,(shipWidth,shipHeight))
spaceship1=pygame.transform.rotate(spaceship1,90)

spaceship2=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/python pro game developer/images/space ship 2.png")
spaceship2=pygame.transform.scale(spaceship2,(shipWidth,shipHeight))
spaceship2=pygame.transform.rotate(spaceship2,270)

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
    font=pygame.font.SysFont("Aptos",55)
    text=font.render(str(ship1health),True,(0,0,0))
    sc.blit(text,(0,0))
    font1=pygame.font.SysFont("Aptos",55)
    text=font1.render(str(ship2health),True,(0,0,0))
    sc.blit(text,(470,0))
    pygame.display.update()

    

draw(ship1rect,ship2rect)

def moveship1(keypress,shiprect1):
    if keypress[pygame.K_a]:
       shiprect1.x=shiprect1.x-10



while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    keypress=pygame.key.get_pressed()
    moveship1(keypress,ship1rect)
    pygame.display.update()