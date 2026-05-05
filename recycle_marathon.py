import pygame
import random
pygame.init()

score=0
framespeed=1000
clock=pygame.time.Clock()
sc=pygame.display.set_mode((900,600))
background=pygame.image.load(r"C:\Users\31mschwarz\OneDrive - Abbey Gate College\python pro game developer\images\recycle_bg.png")
background=pygame.transform.scale(background,(900,600))
sc.blit(background,(0,0))
pygame.display.update()

class bin(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image=pygame.image.load(r"C:\Users\31mschwarz\OneDrive - Abbey Gate College\python pro game developer\images\bin.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

recycleable_images=[r"C:\Users\31mschwarz\OneDrive - Abbey Gate College\python pro game developer\images\paper bag.png",r"C:\Users\31mschwarz\OneDrive - Abbey Gate College\python pro game developer\images\pencil.png",r"C:\Users\31mschwarz\OneDrive - Abbey Gate College\python pro game developer\images\wooden box.png"]
nonrecycleable_image=r"C:\Users\31mschwarz\OneDrive - Abbey Gate College\python pro game developer\images\plastic bag.png"
class recycleable(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image=pygame.image.load(random.choice(recycleable_images))
        self.image=pygame.transform.scale(self.image,(30,50))
        self.rect=self.image.get_rect()

class non_r(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image=pygame.image.load(nonrecycleable_image)
        self.image=pygame.transform.scale(self.image,(30,50))
        self.rect=self.image.get_rect()


recycle=pygame.sprite.Group()
non_recycle=pygame.sprite.Group()
all_items=pygame.sprite.Group()
bin1=bin()
for i in range(40):
    x=random.randint(20,880)
    y=random.randint(20,580)
    r=recycleable()
    r.rect.x=x
    r.rect.y=y
    recycle.add(r)
    all_items.add(r)
for i in range(20):
    x=random.randint(20,880)
    y=random.randint(20,580)
    n=non_r()
    n.rect.x=x
    n.rect.y=y
    non_recycle.add(n)
    all_items.add(n)
all_items.add(bin1)


while True:
     clock.tick(framespeed)
     keypress=pygame.key.get_pressed()
     if keypress[pygame.K_UP]:
         if bin1.rect.y>10:
           bin1.rect.y=bin1.rect.y-1
     if keypress[pygame.K_DOWN]:
         if bin1.rect.y<590:
             bin1.rect.y=bin1.rect.y+1
     if keypress[pygame.K_RIGHT]:
         if bin1.rect.x<890:
             bin1.rect.x=bin1.rect.x+1
     if keypress[pygame.K_LEFT]:
         if bin1.rect.x>10:
             bin1.rect.x=bin1.rect.x-1
     sc.blit(background,(0,0))
     all_items.draw(sc)
     point=pygame.sprite.spritecollide(bin1,recycle,True)
     minus_point=pygame.sprite.spritecollide(bin1,non_recycle,True)
     pygame.display.update()
     for i in point:
         score=score+1
         font=pygame.font.SysFont("Aptos",155)
         text=font.render(str(score),True,(0,0,0))
         sc.blit(text,(880,580))
     for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
