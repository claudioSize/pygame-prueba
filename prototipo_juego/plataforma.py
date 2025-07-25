import pygame
from constantes import NEGRO

class PlataformaGravedad(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect(topleft=(x, y))