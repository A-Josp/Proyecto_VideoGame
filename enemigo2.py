import pygame
import random

class Enemigo2(pygame.sprite.Sprite):
    def __init__(self, dc_game):
        super().__init__()
        self.screen = dc_game.screen
        self.ajustes = dc_game.ajustes
        self.image = pygame.image.load('path/to/your/enemy2_image.png')  # Cambia esta ruta a la de tu imagen
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(10, dc_game.ajustes.anchura - self.rect.width)
        self.rect.y = random.choice([-self.rect.height, dc_game.ajustes.altura])  # Aparece arriba o abajo
        self.velocidad = self.ajustes.velocidadEnemigo * 1.5  # Ajusta la velocidad si deseas

    def update(self):
        if self.rect.y < 0:
            self.rect.y += self.velocidad
        else:
            self.rect.y -= self.velocidad

        if self.rect.top > self.screen.get_height() or self.rect.bottom < 0:
            self.kill()  # Elimina el enemigo de todos los grupos
