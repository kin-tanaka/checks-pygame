import pygame


VELOCIDADE_NAVE = 250  # pixels por segundo


def recebe_eventos():
    # Fecha o jogo quando a janela é encerrada.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def desenha(window, assets, posicao_nave, fps):
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    vermelho = (255, 0, 0)

    window.fill(preto)

    # Desenha o cenário e a nave na posição atual.
    for posicao in [(500, 80), (50, 120), (180, 200), (400, 320), (90, 400)]:
        pygame.draw.circle(window, branco, posicao, 5)

    nave = assets["nave"]
    rect_nave = nave.get_rect(center=posicao_nave)
    window.blit(nave, rect_nave)

    # Mostra as vidas e o FPS nos cantos da janela.
    coracoes = chr(9829) * 3
    img_coracoes = assets["fonte_game"].render(coracoes, True, vermelho)
    window.blit(img_coracoes, (10, 20))

    img_fps = assets["fonte_fps"].render(f"FPS: {fps:.0f}", True, branco)
    rect_fps = img_fps.get_rect(bottomright=(window.get_width() - 10, window.get_height() - 10))
    window.blit(img_fps, rect_fps)

    pygame.display.update()


def game_loop(window, assets):
    relogio = pygame.time.Clock()
    posicao_nave = [window.get_width() / 2, window.get_height() / 2]
    metade_largura = assets["nave"].get_width() / 2
    metade_altura = assets["nave"].get_height() / 2

    while recebe_eventos():
        # delta_tempo permite mover a nave à mesma velocidade com FPS diferentes.
        delta_tempo = relogio.tick(60) / 1000

        # O teclado altera apenas a velocidade; não altera a posição diretamente.
        teclas = pygame.key.get_pressed()
        velocidade_x = (teclas[pygame.K_RIGHT] - teclas[pygame.K_LEFT]) * VELOCIDADE_NAVE
        velocidade_y = (teclas[pygame.K_DOWN] - teclas[pygame.K_UP]) * VELOCIDADE_NAVE

        # Atualiza a posição usando a velocidade e mantém a nave dentro da janela.
        posicao_nave[0] += velocidade_x * delta_tempo
        posicao_nave[1] += velocidade_y * delta_tempo
        posicao_nave[0] = max(metade_largura, min(posicao_nave[0], window.get_width() - metade_largura))
        posicao_nave[1] = max(metade_altura, min(posicao_nave[1], window.get_height() - metade_altura))

        desenha(window, assets, posicao_nave, relogio.get_fps())
