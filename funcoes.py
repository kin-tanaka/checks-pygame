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
    azul_claro = (116, 172, 223)

    # Define as coordenadas dos retângulos
    cord_rect_azul_cima = ((0, 0), (300, 0), (300, 50), (0, 50))
    cord_rect_branco = ((0, 50), (300, 50), (300, 150), (0, 150))
    cord_rect_azul_baixo = ((0, 150), (300, 150), (300, 200), (0, 200))

    # Desenha os retângulos na tela
    pygame.draw.polygon(window, azul_claro, cord_rect_azul_cima)
    pygame.draw.polygon(window, branco, cord_rect_branco)
    pygame.draw.polygon(window, azul_claro, cord_rect_azul_baixo)

    # Desenha o sol da bandeira da Argentina no centro da tela
    sol = assets["sol_bandeira"]
    sol_formatado = pygame.transform.scale(sol, (100, 100))
    posicao_sol = sol_formatado.get_rect(center=(150, 100))
    window.blit(sol_formatado, posicao_sol)

    # Atualiza a tela
    pygame.display.update()

def game_loop(window, assets):
    # Loop principal do jogo
    game = True

    while game:
        game = recebe_eventos()
        desenha(window, assets)