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
    azul = (0, 0, 255)

    # Preenche a tela com a cor preta
    window.fill(preto)

    # Define o texto a ser exibido
    texto_16 = assets["fonte_16"].render("Fonte tamanho 16", True, branco)
    texto_48 = assets["fonte_48"].render("Fonte tamanho 48", True, azul)

    # Exibe o texto na tela
    window.blit(texto_16, (10, 20))
    window.blit(texto_48, (10, 70))

    # Atualiza a tela
    pygame.display.update()

def game_loop(window, assets):
    # Loop principal do jogo
    game = True

    while game:
        game = recebe_eventos()
        desenha(window, assets)