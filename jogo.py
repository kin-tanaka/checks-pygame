import funcoes
import pygame
import os

# Inicialização
pygame.init()

# Carrega os assets do jogo
assets = {
    "fonte_16" : pygame.font.Font(pygame.font.get_default_font(), 16),
    "fonte_48" : pygame.font.Font(pygame.font.get_default_font(), 48)
}

# Gera tela principal
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Jogo do KIN')

# Loop principal do jogo
jogo = funcoes.game_loop(window, assets)