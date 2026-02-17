import pygame
import time
pygame.init()
sc=pygame.display.set_mode((500,500))
pygame.display.set_caption("Birthday Card")
sc.fill("white")
pygame.display.update()

birthdaymessege=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/python pro game developer/images/happy birthday.webp")
birthdaymessege=pygame.transform.scale(birthdaymessege,(500,500))

birthdaycake=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/python pro game developer/images/birthday cake.png")
birthdaycake=pygame.transform.scale(birthdaycake,(500,500))

birthdaypresents=pygame.image.load("C:/Users/31mschwarz/OneDrive - Abbey Gate College/python pro game developer/images/birthday presents.png")
birthdaypresents=pygame.transform.scale(birthdaypresents,(500,500))




while True:
    sc.blit(birthdaymessege,(0,0))
    pygame.display.update()
    time.sleep(2)
    sc.blit(birthdaycake,(0,0))
    font=pygame.font.SysFont("Aptos",55)
    text=font.render("Happy Birthday",True,(0,0,0))
    sc.blit(text,(0,0))
    pygame.display.update()
    time.sleep(2)
    sc.blit(birthdaypresents,(0,0))
    time.sleep(2)
    text1=font.render("From Max",True,(0,0,0))
    sc.blit(text1,(0,0))
    pygame.display.update()
    time.sleep(2)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()


