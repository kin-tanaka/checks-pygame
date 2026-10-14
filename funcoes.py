import pygame

def recebe_eventos():
    # Verifica os eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window, assets):
    # Define as cores
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    vermelho = (255, 0, 0)

    # Preenche a tela com a cor preta
    window.fill(preto)

    # Desenha estrelas
    pygame.draw.circle(window, branco, (500, 80), 5)
    pygame.draw.circle(window, branco, (50, 120), 5)
    pygame.draw.circle(window, branco, (180, 200), 5)
    pygame.draw.circle(window, branco, (400, 320), 5)
    pygame.draw.circle(window, branco, (90, 400), 5)


    # Desenha a nave no centro da tela
    nave = assets["nave"]
    nave_formatada = pygame.transform.scale(nave, (70, 70))
    posicao_nave = nave_formatada.get_rect(center=(320, 240))
    window.blit(nave_formatada, posicao_nave)

    # Coloca os corações no canto superior esquerdo da tela
    coracoes = chr(9829) * 3
    img_coracoes = assets["fonte_game"].render(coracoes, True, vermelho)

    # Exibe o texto na tela
    window.blit(img_coracoes, (10, 20))

    # Atualiza a tela
    pygame.display.update()

def game_loop(window, assets):
    # Loop principal do jogo
    game = True

    while game:
        game = recebe_eventos()
        desenha(window, assets)