import pygame
from pygame.locals import *
from sys import exit

def processar_eventos():
    dx, dy = 0, 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        dx = -20
    if keys[K_d]:
        dx = 20
    '''if keys[K_w]:
        dy = -20'''
    if keys[K_s]:
        dy = 20
    return dx, dy

def desenha_carro():
    return pygame.image.load('carro.png')
