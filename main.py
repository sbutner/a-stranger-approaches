import pygame, pygame.font, pygame.event, pygame.draw, string,sys
import listener

from pygame.locals import *



####



def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    done = False

    pygame.display.set_caption('A stranger approaches...')

    while 1: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__': main()
