import pygame
from pygame.locals import *
from sys import exit
import sys
import os

# Adiciona o diretório principal ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from carro.carroM import processar_eventos, desenha_carro
from rua.rua import carregar_imagem, desenha_rua, movimento_rua, nova_posicao_buraco

pygame.init()
largura = 640
altura = 480

# Ajuste para passar o caminho correto para a função carregar_imagem
rua_imagem = carregar_imagem(os.path.join('imagens', 'pista.png'))
carro_imagem = carregar_imagem(os.path.join('imagens', 'carro.png'))

y1 = 0
y2 = -altura
x = largura / 2
c = largura / 2
c2 = 420
velocidade_pista = 5
velocidade_carro = 0.5
pista_esquerda = x - 80
pista_direita = x + 140
raio_buraco = 20
x_buraco = nova_posicao_buraco()
y_buraco = -raio_buraco

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CARdGame')
relogio = pygame.time.Clock()

while True:
    relogio.tick(800)
    tela.fill((255, 255, 255))

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        y1 += movimento_rua()
        y2 += movimento_rua()

    if y1 >= altura:
        y1 = -altura
    if y2 >= altura:
        y2 = -altura

    desenha_rua(tela, rua_imagem, y1, y2, x_buraco, y_buraco, raio_buraco)

    y_buraco += 5
    if y_buraco - raio_buraco > altura:
        y_buraco = -raio_buraco
        x_buraco = nova_posicao_buraco()

    '''carro_rect = pygame.Rect(c, c2, 40, 50)'''
    buraco_rect = pygame.Rect(x_buraco - raio_buraco, y_buraco - raio_buraco, raio_buraco * 2, raio_buraco * 2)

    dx, dy = processar_eventos()
    novo_x = c + dx * velocidade_carro
    novo_y = c2 + dy * velocidade_carro

    if pista_esquerda < novo_x < pista_direita - 40:
        c = novo_x
    if 0 < novo_y < altura - 50:
        c2 = novo_y

    tela.blit(carro_imagem, (c, c2))

    pygame.display.update()
