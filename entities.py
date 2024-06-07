import pygame as pg

from physics import * 

class Ball: #pg.Sprite.sprite
    def __init__(self, game):
        #super().__init__(group)
        self.game = game
        
        self.velo = [0,0]
        
        self.pos = [0, 0]
        
        self.image = pg.image.load('images/balls/ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.screen.get_width()//2, self.game.screen.get_height()//2)
        
    def physics(self, tilemap, posi, velo, direction, state):
        if self.game.shoot:
            power = self.game.shoot
            self.game.shoot = None   
        print(tilemap.rects_around)


        
        direction ,self.velo = bounce(state, direction, velo)
        direction = acvel(power,direction,velo)[2]
        velo = acvel(power,direct,velo)[0]
        posi = position(velo, posi)

        power = force(acvel(f,direct,velo)[1])

        
        
    
    def physics(self, tilemap):
        ball_rect = pg.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())
        if self.game.shoot:
            power = self.game.shoot
            self.game.shoot = None   
        #print(tilemap.rects_around(self.pos))
        #print(ball_rect)
        for rect in tilemap.rects_around(self.pos):
            if rect.colliderect(ball_rect):
               pass
            
        
        
    
    def render(self, surf):
        surf.blit(self.image, self.rect)