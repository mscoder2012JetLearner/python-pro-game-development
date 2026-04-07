import pygame
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
        
    
bin1=bin()


while True:
     for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
