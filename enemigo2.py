import pygame
import os
import random

class Enemigo2(pygame.sprite.Sprite):
    def __init__(self, dc_game):
        super().__init__()
        self.screen = dc_game.screen
        self.ajustes = dc_game.ajustes

        # Cargar los frames del enemigo
        self.frames = self.cargar_frames('frames2')  # Cambia 'frames2' por la carpeta donde estén los frames de este enemigo
        self.frame_actual = 0
        self.image = self.frames[self.frame_actual]
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(10, dc_game.ajustes.anchura - self.rect.width)
        self.rect.y = random.choice([-self.rect.height, dc_game.ajustes.altura])  # Aparece arriba o abajo
        self.velocidad = self.ajustes.velocidadEnemigo * 1.5  # Puedes ajustar la velocidad si deseas

    def cargar_frames(self, carpeta):
        frames = []
        for archivo in sorted(os.listdir(carpeta)):
            if archivo.endswith('.png'):
                ruta = os.path.join(carpeta, archivo)
                frames.append(pygame.image.load(ruta))
        return frames

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > self.screen.get_height() or self.rect.bottom < 0:
            self.kill()  # Elimina el enemigo de todos los grupos

        # Actualizar el frame actual del enemigo
        self.frame_actual = (self.frame_actual + 1) % len(self.frames)
        self.image = self.frames[self.frame_actual]
