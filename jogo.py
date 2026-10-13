import funcoes
import pygame
import os

# Inicialização
pygame.init()

# Carrega os assets do jogo
assets = {
    "sol_bandeira": pygame.image.load(os.path.join("assets/img/ex_check2", "sol_bandeira_argentina.jpg"))
}

# Gera tela principal
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Jogo do KIN')

# Loop principal do jogo
jogo = funcoes.game_loop(window, assets)