import pygame

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window):
    window.fill((255, 0, 0))
    pygame.display.update()

def game_loop(window):
    game = True

    while game:
        game = recebe_eventos()
        desenha(window)