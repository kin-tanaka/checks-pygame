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
    azul_claro = (160, 185, 255)

    # Define as coordenadas dos retângulos
    cord_rect_azul_cima = ((0, 0), (640, 0), (640, 120), (0, 120))
    cord_rect_branco = ((0, 120), (640, 120), (640, 360), (0, 360))
    cord_rect_azul_baixo = ((0, 360), (640, 360), (640, 480), (0, 480))

    # Desenha os retângulos na tela
    pygame.draw.polygon(window, azul_claro, cord_rect_azul_cima)
    pygame.draw.polygon(window, branco, cord_rect_branco)
    pygame.draw.polygon(window, azul_claro, cord_rect_azul_baixo)

    # Desenha o sol da bandeira da Argentina no centro da tela
    sol = assets["sol_bandeira"]
    sol_formatado = pygame.transform.scale(sol, (200, 200))
    posicao_sol = sol_formatado.get_rect(center=(320, 240))
    window.blit(sol_formatado, posicao_sol)

    # Atualiza a tela
    pygame.display.update()

def game_loop(window, assets):
    # Loop principal do jogo
    game = True

    while game:
        game = recebe_eventos()
        desenha(window, assets)