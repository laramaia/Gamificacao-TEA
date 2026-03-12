import pygame

class Sidebar:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.retangulo = pygame.Rect(0, 0, largura, altura)
        self.cor_fundo = "#2B2348" 

    def desenhar(self, screen):
        pygame.draw.rect(screen, self.cor_fundo, self.retangulo)