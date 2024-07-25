import pygame
from pygame.sprite import Sprite
import random

class Enemigo(Sprite):
    def __init__(self, dc_game):
        super().__init__()
        self.screen = dc_game.screen

        # Especifica la ruta correcta de la imagen aquí
        self.image = pygame.image.load('imagenes/cocheR.png')
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height - 50
        self.rect.x = random.randint(10, dc_game.ajustes.anchura - self.rect.width)
        self.ajustes = dc_game.ajustes

    def update(self):
        self.rect.y += self.ajustes.velocidadEnemigo

