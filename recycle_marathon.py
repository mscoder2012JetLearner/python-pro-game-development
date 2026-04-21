import pygame
import random
pygame.init()

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
class recycleable(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image=pygame.image.load(random.choice(recycleable_images))
        self.image=pygame.transform.scale(self.image,(30,50))
        self.rect=self.image.get_rect()


all_items=pygame.sprite.Group()
bin1=bin()
for i in range(40):
    x=random.randint(20,880)
    y=random.randint(20,580)
    r=recycleable()
    r.rect.x=x
    r.rect.y=y
    all_items.add(r)
all_items.add(bin1)


while True:
     all_items.draw(sc)
     pygame.display.update()
     for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
