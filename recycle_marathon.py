import pygame
import random
import time
pygame.init()

starting_time=time.time()
score=0
framespeed=60
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
     time_changed=time.time()
     differance=time_changed-starting_time
     if differance>35:
         if score>25:
             score_message=font.render("You Win!",True,(0,0,0))
             sc.blit(score_message,(400,400))
         else:
             score_message=font.render("You Loose",True,(0,0,0))
             sc.blit(score_message,(400,400))
     clock.tick(framespeed)
     keypress=pygame.key.get_pressed()
     if keypress[pygame.K_UP]:
         if bin1.rect.y>10:
           bin1.rect.y=bin1.rect.y-4
     if keypress[pygame.K_DOWN]:
         if bin1.rect.y<590:
             bin1.rect.y=bin1.rect.y+4
     if keypress[pygame.K_RIGHT]:
         if bin1.rect.x<890:
             bin1.rect.x=bin1.rect.x+4
     if keypress[pygame.K_LEFT]:
         if bin1.rect.x>10:
             bin1.rect.x=bin1.rect.x-4
     point=pygame.sprite.spritecollide(bin1,recycle,True)
     minus_point=pygame.sprite.spritecollide(bin1,non_recycle,True)
     for i in point:
         score=score+1
     font=pygame.font.SysFont("Aptos",35)
     for i in minus_point:
         score=score-3
     text=font.render("score="+str(score),True,(0,0,0))
     sc.blit(background,(0,0))
     all_items.draw(sc)
     sc.blit(text,(15,15))   
     t=font.render("time="+str(int(differance)),True,(0,0,0))
     sc.blit(t,(725,35))
     pygame.display.update()    
     for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
