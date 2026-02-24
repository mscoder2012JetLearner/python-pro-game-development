import pygame
import time
pygame.init()
sc=pygame.display.set_mode((500,500))
pygame.display.set_caption("lightbulb")
sc.fill("white")
pygame.display.update()

bulbon=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/Documents and subjects/python game developer/images/lightbulb_on.png")
bulbon=pygame.transform.scale(bulbon,(500,500))

bulboff=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/Documents and subjects/python game developer/images/lightbulb off.jpg")
bulboff=pygame.transform.scale(bulboff,(500,500))

while True:
    sc.blit(bulbon,(0,0))
    pygame.display.update()
    time.sleep(2)
    sc.blit(bulboff,(0,0))
    pygame.display.update()
    time.sleep(2)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
