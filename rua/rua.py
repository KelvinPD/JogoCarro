import pygame
from pygame.locals import *
from sys import exit
import random

largura = 640
altura = 480
x_centro_rua = largura // 2
largura_rua = 300
raio_buraco = 30

def carregar_imagem():
    return pygame.image.load('minha_rua.png')

def desenha_rua(tela, rua_imagem, y1, y2, buraco_x, buraco_y, buraco_raio):
    tela.blit(rua_imagem, (0, y1))
    tela.blit(rua_imagem, (0, y2))
    pygame.draw.circle(tela, (255, 255, 255), (buraco_x, buraco_y), buraco_raio + 3)  # Bordas do buraco
    pygame.draw.circle(tela, (0, 0, 0), (buraco_x, buraco_y), buraco_raio)  # Buraco

def movimento_rua():
    return 5

def nova_posicao_buraco():
    return random.randint(x_centro_rua - largura_rua // 2 + raio_buraco, x_centro_rua + largura_rua // 2 - raio_buraco)
