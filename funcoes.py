import pygame

def recebe_eventos():
    # Verifica os eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window, assets):
    # Define as cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)

    window.fill(preto)

    pygame.draw.circle(window, branco, (500, 80), 10)
    pygame.draw.circle(window, branco, (50, 10), 10)
    pygame.draw.circle(window, branco, (180, 200), 10)
    pygame.draw.circle(window, branco, (400, 320), 10)
    pygame.draw.circle(window, branco, (90, 400), 10)


    # Desenha a nave no centro da tela
    nave = assets["nave"]
    nave_formatada = pygame.transform.scale(nave, (70, 70))
    posicao_sol = nave_formatada.get_rect(center=(320, 240))
    window.blit(nave_formatada, posicao_sol)

    # Atualiza a tela
    pygame.display.update()

def game_loop(window, assets):
    # Loop principal do jogo
    game = True

    while game:
        game = recebe_eventos()
        desenha(window, assets)