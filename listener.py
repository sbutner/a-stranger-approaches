import pygame, pygame.font, pygame.event, pygame.draw, string,sys
from pygame.locals import *




def listen():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def displayTicker(screen, text):
    fontobject = pygame.font.Font(None,18)
    screen.blit(fontobject.render(text,1, (255,255,255)),((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()
def takeInput(screen, current_string):
    current_string
    while 1:
        keyin = listen()
        if keyin == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif keyin == K_RETURN:
            break
        elif keyin == K_MINUS:
            current_string.append("_")
        elif keyin <= 127:
            current_string.append(chr(keyin))
    return current_string
def updateTicker(screen, text):
    display_box(screen, ">".join(text))



def listenLoop(screen, stringList):
    listen()
    textin = takeInput(screen, stringList)
    displayTicker(screen, stringList)
