import pygame
from constantes import ANCHO, ALTO, VERDE, NARANJA, COLOR_ORIGINAL
from player import Player
from coin import Coin
from plataforma import PlataformaGravedad

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("El regreso de la moneda asesina")
icono = pygame.image.load("assets/icono.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("assets/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
explosion_img = pygame.image.load("assets/explosion.png").convert_alpha()

clock = pygame.time.Clock()

jugador = Player()
monedas = pygame.sprite.Group()
todas_las_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()

todas_las_sprites.add(jugador)

moneda1 = Coin(200, ALTO - 60)
moneda2 = Coin(300, ALTO - 60)
moneda_extra1 = Coin(400, ALTO - 60)
monedas.add(moneda1, moneda2, moneda_extra1)
todas_las_sprites.add(moneda1, moneda2, moneda_extra1)

obstaculo_suelo = PlataformaGravedad(250, ALTO - 100)
plataformas.add(obstaculo_suelo)
todas_las_sprites.add(obstaculo_suelo)

moneda3 = Coin(30, 30)
moneda4 = Coin(ANCHO - 30, 30)
moneda_extra2 = Coin(ANCHO // 2, 40)
monedas.add(moneda3, moneda4, moneda_extra2)
todas_las_sprites.add(moneda3, moneda4, moneda_extra2)

obstaculo_arriba = PlataformaGravedad(ANCHO - 80, 80)
plataformas.add(obstaculo_arriba)
todas_las_sprites.add(obstaculo_arriba)

contador_monedas = 0
fuente = pygame.font.SysFont(None, 36)

ejecutando = True
while ejecutando:
    keys = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if not jugador.explotado:
                if evento.key == pygame.K_b:
                    jugador.image.fill(VERDE)
                elif evento.key == pygame.K_n:
                    jugador.image.fill(NARANJA)
                elif evento.key == pygame.K_m:
                    jugador.image.fill(COLOR_ORIGINAL)

    if not jugador.explotado:
        jugador.update(keys)

    colisiones = pygame.sprite.spritecollide(jugador, monedas, True)
    if colisiones:
        contador_monedas += len(colisiones)

    if contador_monedas >= 6 and not jugador.explotado:
        jugador.explotar(explosion_img)

    if not jugador.explotado:
        if jugador.rect.colliderect(obstaculo_suelo.rect):
            jugador.gravedad = -1
            jugador.velocidad_y = 0
        elif jugador.rect.colliderect(obstaculo_arriba.rect):
            jugador.gravedad = 1
            jugador.velocidad_y = 0

    pantalla.blit(fondo, (0, 0))
    todas_las_sprites.draw(pantalla)

    texto = fuente.render(f"Monedas: {contador_monedas}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
