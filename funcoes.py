import pygame
import os


# Inicializa o Pygame
def inicializa():
    pygame.init()

    # Gera tela principal
    window = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Jogo do KIN')

    # Carrega os assets do jogo
    assets = {
        'jogador': pygame.image.load(os.path.join('assets/img/ex_movimentacao', 'player.png'))
    }

    state = {
        'jogador_x': window.get_width() // 2,
        'jogador_y': window.get_height() // 2
    }

    return window, assets, state


# Verifica os eventos do jogo
def recebe_eventos(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                state['jogador_x'] += 10
            elif event.key == pygame.K_LEFT:
                state['jogador_x'] -= 10
            elif event.key == pygame.K_UP:
                state['jogador_y'] -= 10
            elif event.key == pygame.K_DOWN:
                state['jogador_y'] += 10

    return True


# Desenha os elementos na tela
def desenha(window, assets, state):
    # Define as cores
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    azul = (0, 0, 255)

    # Preenche a tela com a cor preta
    window.fill(branco)

    jogador = assets['jogador']
    posicao_jogador = jogador.get_rect(center = (state['jogador_x'], state['jogador_y']))
    window.blit(jogador, posicao_jogador)

    # Atualiza a tela
    pygame.display.update()


# Loop principal do jogo
def game_loop(window, assets, state):
    game = True

    while game:
        game = recebe_eventos(state)
        desenha(window, assets, state)