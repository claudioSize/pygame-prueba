import pygame
from constantes import COLOR_ORIGINAL, ALTO

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = COLOR_ORIGINAL
        self.image.fill(self.color)
        self.rect = self.image.get_rect(midbottom=(100, ALTO))
        self.velocidad_y = 0
        self.gravedad = 1
        self.velocidad_x = 5
        self.saltando = False
        self.explotado = False

    def update(self, keys):
        if self.explotado:
            return

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.velocidad_x
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.velocidad_x
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and not self.saltando:
            self.velocidad_y = -15 * self.gravedad
            self.saltando = True

        self.velocidad_y += 1 * self.gravedad
        self.rect.y += self.velocidad_y

        if self.rect.bottom >= ALTO:
            self.rect.bottom = ALTO
            self.velocidad_y = 0
            self.saltando = False

        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocidad_y = 0
            self.saltando = False

        self.image.fill(self.color)

    def explotar(self, imagen_explosion):
        self.image = pygame.transform.scale(imagen_explosion, (50, 50))
        self.explotado = True