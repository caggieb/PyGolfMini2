import pygame as pg

from physics import * 

class Ball: #pg.Sprite.sprite
    def __init__(self, game):
        #super().__init__(group)
        self.game = game
        self.pos = pg.math.Vector2(0, 0)
        self.velo = [0,0]
        
        
        self.image = pg.image.load('images/balls/ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.screen.get_width()//2, self.game.screen.get_height()//2)
        
    def physics(self, tilemap, direction):
        if self.game.shoot:
            power = self.game.shoot
            self.game.shoot = None   
        print(tilemap.rects_around)

        
        direction ,self.velo = bounce(state, direct, velo)
        direction = acvel(f,direct,velo)[2]
        velo = acvel(f,direct,velo)[0]
        posi = position(velo, posi)

        f = force(acvel(f,direct,velo)[1])
        
        power = force(acvel(f,direct,velo)[1])
    
        #if self.pos in tilemap.rects_around:
        #    print('gino')
            
        
    
    def render(self, surf):
        surf.blit(self.image, self.rect)