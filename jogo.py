import funcoes
import pygame

# Inicialização
pygame.init()

# Gera tela principal
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Jogo do KIN')

jogo = funcoes.game_loop(window)