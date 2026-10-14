import funcoes
import pygame
from pathlib import Path

# Inicialização
pygame.init()

PASTA_PROJETO = Path(__file__).resolve().parent

# Carrega os assets do jogo
assets = {
    "fonte_game": pygame.font.Font(PASTA_PROJETO / 'assets/font/PressStart2P.ttf', 20),
    "fonte_fps": pygame.font.Font(PASTA_PROJETO / 'assets/font/PressStart2P.ttf', 12),
    "nave": pygame.transform.scale(
        pygame.image.load(PASTA_PROJETO / 'assets/img/playerShip1_orange.png'), (70, 70)
    ),
}

# Gera tela principal
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Jogo do KIN')

# Loop principal do jogo
funcoes.game_loop(window, assets)
pygame.quit()
