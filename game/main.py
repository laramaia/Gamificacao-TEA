import sys
import pygame
from telas.mapa import Mapa

sys.dont_write_bytecode = True

pygame.init()

LARGURA = 1280
ALTURA = 680

screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Gamificação TEA")

clock = pygame.time.Clock()
tela_atual = Mapa()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

        nova_tela = tela_atual.handle_event(event)
        if nova_tela is not None:
            tela_atual = nova_tela

    tela_atual.update()
    tela_atual.desenhar(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()