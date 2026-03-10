import pygame
pygame.font.init()
pygame.init()
sc=pygame.display.set_mode((900,500))
maxbullets=3
bulletspeed=7
shipWidth=55
shipHeight=40
ship1health=10
ship2health=10
framespersecond=60
clock=pygame.time.Clock()

ship1bullets=[]
ship2bullets=[]

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
    for i in ship1bullets:
       pygame.draw.rect(sc,"red",i)
    for t in ship2bullets:
       pygame.draw.rect(sc,"yellow",t)
    pygame.display.update()

    


def moveship1(keypress,shiprect1):
    if keypress[pygame.K_a]:
       if shiprect1.x>0:
          shiprect1.x=shiprect1.x-6
    if keypress[pygame.K_d]:
       if shiprect1.x<400:
          shiprect1.x=shiprect1.x+6
    if keypress[pygame.K_w]:
       if shiprect1.y>0:
          shiprect1.y=shiprect1.y-6
    if keypress[pygame.K_s]:
       if shiprect1.y<450:
          shiprect1.y=shiprect1.y+6

def moveship2(keypress,shiprect2):
    if keypress[pygame.K_LEFT]:
       if shiprect2.x>450:
          shiprect2.x=shiprect2.x-6
    if keypress[pygame.K_RIGHT]:
       if shiprect2.x<850:
          shiprect2.x=shiprect2.x+6
    if keypress[pygame.K_UP]:
       if shiprect2.y>0:
          shiprect2.y=shiprect2.y-6
    if keypress[pygame.K_DOWN]:
       if shiprect2.y<450:
          shiprect2.y=shiprect2.y+6

def movebullet(ship1bullets,ship2bullets):
   for bullets in ship1bullets:
      bullets.x=bullets.x+bulletspeed
      if bullets.x>=900:
         ship1bullets.remove(bullets)
   for bullets in ship2bullets:
      bullets.x=bullets.x-bulletspeed
      if bullets.x<=0:
         ship2bullets.remove(bullets)

while True:
    clock.tick(framespersecond)
    keypress=pygame.key.get_pressed()
    moveship1(keypress,ship1rect)
    moveship2(keypress,ship2rect)
    draw(ship1rect,ship2rect)
    movebullet(ship1bullets,ship2bullets)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    if keypress[pygame.K_LCTRL] and len(ship1bullets)<maxbullets:
       bullet=pygame.Rect(ship1rect.x+55,ship1rect.y+20,10,5)
       ship1bullets.append(bullet)
    if keypress[pygame.K_RCTRL] and len(ship2bullets)<maxbullets:
      bullet=pygame.Rect(ship2rect.x,ship2rect.y+20,10,5)
      ship2bullets.append(bullet)
    
       

