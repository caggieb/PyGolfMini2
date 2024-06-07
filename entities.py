import pygame as pg

from physics import * 

class Ball: #pg.Sprite.sprite
    def __init__(self, game):
        #super().__init__(group)
        self.game = game
        self.pos = [0, 0]
        
        self.image = pg.image.load('images/balls/ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.screen.get_width()//2, self.game.screen.get_height()//2)
        
    def physics(self, tilemap):
        
        
        if self.game.shoot:
            power = self.game.shoot
            self.game.shoot = None   
        #print(tilemap.rects_around(self.pos))
        #if self.pos in tilemap.rects_around:
        #    print('gino')
        
        
    
    def render(self, surf):
        surf.blit(self.image, self.rect)