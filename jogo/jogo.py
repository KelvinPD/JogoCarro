import pygame
from pygame.locals import *
from sys import exit
import sys
import os
import random

# Adiciona o diretório principal ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from carro.carroM import processar_eventos, desenha_carro
from rua.rua import carregar_imagem, desenha_rua, movimento_rua, nova_posicao_buraco

pygame.init()
largura = 640
altura = 480

# Carregue a nova imagem do carro
rua_imagem = carregar_imagem(os.path.join('imagens', 'pista5.png'))
carro_imagem = carregar_imagem(os.path.join('imagens', 'carro5.png'))

if not carro_imagem:
    print("Erro ao carregar imagem do carro")

carro_imagem = pygame.transform.scale(carro_imagem, (140, 80))
rua_imagem = pygame.transform.scale(rua_imagem, (640, 480))

y1 = 0
y2 = -altura
x = largura / 2
c = largura / 2
c2 = 420
velocidade_pista = 5
velocidade_carro = 0.5
pista_esquerda = 180
pista_direita = 482
raio_buraco = 20
x_buraco = nova_posicao_buraco(pista_esquerda, pista_direita, raio_buraco)
y_buraco = -raio_buraco  # Inicialmente fora da tela

# Contador para frequência do buraco
contador_buraco = 0
frequencia_buraco = 200  # Ajuste conforme necessário para controlar a frequência

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CARdGame')
relogio = pygame.time.Clock()

while True:
    relogio.tick(600)  # Ajustando para 60 FPS
    tela.fill((255, 255, 255))

    keys = pygame.key.get_pressed()
    dx, dy = processar_eventos()  # Certifique-se de que dx e dy estão definidos antes do if

    if dy != 0:  # Se o carro estiver se movendo
        y1 += movimento_rua()
        y2 += movimento_rua()
        if contador_buraco >= frequencia_buraco:  # Movimentação do buraco baseada no contador
            y_buraco += velocidade_pista

    if y1 >= altura:
        y1 = -altura
    if y2 >= altura:
        y2 = -altura

    desenha_rua(tela, rua_imagem, y1, y2, x_buraco, y_buraco, raio_buraco)

    if y_buraco - raio_buraco > altura:  # Reposicione o buraco quando sair da tela
        y_buraco = -raio_buraco
        x_buraco = nova_posicao_buraco(pista_esquerda + 40, pista_direita - 40, raio_buraco)
        contador_buraco = 0  # Redefine o contador após reposicionar o buraco

    carro_rect = pygame.Rect(c, c2, carro_imagem.get_width(), carro_imagem.get_height())
    buraco_rect = pygame.Rect(x_buraco - raio_buraco, y_buraco - raio_buraco, raio_buraco * 2, raio_buraco * 2)

    novo_x = c + dx * velocidade_carro
    novo_y = c2 + dy * velocidade_carro

    if pista_esquerda < novo_x < pista_direita - carro_imagem.get_width():
        c = novo_x
    if 0 < novo_y < altura - carro_imagem.get_height():
        c2 = novo_y

    tela.blit(carro_imagem, (c, c2 - 50))
    pygame.display.update()

    contador_buraco += 1
