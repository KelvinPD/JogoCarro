import pygame
from pygame.locals import *
from sys import exit
import carroM
import Rua

pygame.init()

largura = 640
altura = 480
rua_imagem = Rua.carregar_imagem()
y1 = 0
y2 = -altura
b = altura
x = largura / 2
y = altura / 2
c = largura / 2
c2 = 420
velocidade_pista = 5
velocidade_carro = 0.5
pista_esquerda = x - 161
pista_direita = x + 169
raio_buraco = 20
x_buraco = Rua.nova_posicao_buraco()
y_buraco = -Rua.raio_buraco

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CARdGame')
relogio = pygame.time.Clock()

while True:
    relogio.tick(50)
    tela.fill((255, 255, 255))

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        y1 += Rua.movimento_rua()
        y2 += Rua.movimento_rua()

    if y1 >= altura:
        y1 = -altura
    if y2 >= altura:
        y2 = -altura

    Rua.desenha_rua(tela, rua_imagem, y1, y2, x_buraco, y_buraco, Rua.raio_buraco)

    y_buraco += 5
    if y_buraco - Rua.raio_buraco > altura:
        y_buraco = -Rua.raio_buraco
        x_buraco = Rua.nova_posicao_buraco()

    carro_rect = pygame.Rect(c, c2, 40, 50)
    buraco_rect = pygame.Rect(x_buraco - Rua.raio_buraco, y_buraco - Rua.raio_buraco, Rua.raio_buraco * 2, Rua.raio_buraco * 2)

    dx, dy = carroM.processar_eventos()
    novo_x = c + dx * velocidade_carro
    novo_y = c2 + dy * velocidade_carro

    if pista_esquerda < novo_x < pista_direita - 40:
        c = novo_x
    if 0 < novo_y < altura - 50:
        c2 = novo_y

    carroM.desenha_carro(tela, carro_imagem, c, c2)

    pygame.display.update()
