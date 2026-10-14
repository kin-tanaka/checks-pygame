import funcoes
import pygame
import os

# Inicialização
pygame.init()

# Carrega os assets do jogo
assets = {
    "nave": pygame.image.load('assets/img/playerShip1_orange.png')
}

# Gera tela principal
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Jogo do KIN')

# Loop principal do jogo
jogo = funcoes.game_loop(window, assets)