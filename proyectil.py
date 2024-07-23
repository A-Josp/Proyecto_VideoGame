import pygame
from pygame.sprite import Sprite

class bala(Sprite):
    def _init_(self,dc_game):
        super()._init_()
        self.screen = dc_game
        self.ajustes = dc_game.ajustes
        self.color = self.ajustes.colorBala
        self.rect = pygame.Rect(0,0,self.ajustes.anchuraBala, self.ajustes.alturaBala)
        self.rect.midtop = dc_game.coche.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.ajustes.velocidadBala
        self.rect.y = self.y

    def pintarBala(self):
        pygame.draw.rect(self.screen,self.color,self.rect)     

     #Esto va en ajustes
     #balas
        self.velocidadBala = 3
        self.anchuraBala =  1
        self.alturaBala=14
        self.colorBala=(11,255,255)
        self.balasPermitidad =  6
