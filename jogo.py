import funcoes


# Inicializa o jogo e entra no loop principal, atualizando o estado e desenhando a tela
window, assets, state = funcoes.inicializa()
while funcoes.atualiza_estado(state):
    funcoes.desenha(window, assets, state)