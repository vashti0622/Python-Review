import pygame
pygame.init() 
size = width, height = 700,500
screen = pygame.display.set_mode(size)
#Write a program that moves a circle across a screen, horizontally

#color
WHITE = (255,255,255)
BLACK = (0,0,0)
#background
screen.fill((BLACK))

#motion of the circle
running = True
count=0
while running == True:
    for x in range (0, 700):
        pygame.draw.circle(screen,WHITE,(x,250),15)
        pygame.time.wait(1)
        pygame.display.flip()
        screen.fill((BLACK))
    count += 1
    print (count)
    if count >= 3:
        running = False
    
pygame.quit()