import pygame
from telas.mapa import Mapa
import sys

sys.dont_write_bytecode = True

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

tela_atual = Mapa()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        tela_atual.handle_event(event)

    tela_atual.update()
    tela_atual.desenhar(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()