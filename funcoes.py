import pygame


# Inicializa o Pygame, cria a janela e define o estado inicial do jogo
def inicializa():
    pygame.init()
    window = pygame.display.set_mode((640, 480), vsync=True, flags=pygame.SCALED)

    assets = {
    }

    state = {
        'ball_pos': [100, 150],
        'ball_vel': [400, 300],  # pixels per second
        'last_updated': 0
    }

    return window, assets, state


# Desenha a bola na tela com base na posição atual
def desenha(window: pygame.Surface, assets, state):
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 0, 0), state['ball_pos'], 10)
    pygame.display.update()


# Atualiza a posição da bola com base na velocidade e no tempo decorrido
def atualiza_estado(state):
    t1 = pygame.time.get_ticks() / 1000
    dt = t1 - state['last_updated']

    state['ball_pos'][0] += dt * state['ball_vel'][0]
    state['ball_pos'][1] += dt * state['ball_vel'][1]

    if state['ball_pos'][0] < 10 or state['ball_pos'][0] > 630:
        state['ball_vel'][0] *= -1
    if state['ball_pos'][1] < 10 or state['ball_pos'][1] > 470:
        state['ball_vel'][1] *= -1

    state['last_updated'] = t1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True