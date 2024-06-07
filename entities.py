import pygame as pg

from physics import * 

class Ball: #pg.Sprite.sprite
    def __init__(self, game):
        #super().__init__(group)
        self.game = game
        self.power = 0
        
        self.pos = [0, 0]
        
        self.image = pg.image.load('images/balls/ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.screen.get_width()//2, self.game.screen.get_height()//2)
        
        self.velocity = [0,0]
        
        
        
    def physics(self, tilemap, direction, state = None, surf = None):
        ball_rect = pg.Rect(self.pos[0] - self.image.get_width()/2, self.pos[1] - self.image.get_height()/2, self.image.get_width(), self.image.get_height())
        
        if self.game.shoot:
            self.power = (self.game.shoot**0.5)
            self.game.shoot = None   
            
        
        rects, end_rect = tilemap.rects_around(self.pos)
        for rect in rects:
            if ball_rect.colliderect(rect):
                if  int(self.pos[0] - self.image.get_width()) <= rect.left <= int(self.pos[0] + self.image.get_width()):
                    state = 'vertical'
                
                elif int(self.pos[0] + self.image.get_width()) >= rect.right >= int(self.pos[0] - self.image.get_width()):
                    state = 'vertical'
                    
                if int(self.pos[1] + self.image.get_width()) >= rect.top >= int(self.pos[1] - self.image.get_width()):
                    state = 'horizontal'
                elif int(self.pos[1] - self.image.get_width()) <= rect.bottom <= int(self.pos[1] + self.image.get_width()):
                    state = 'horizontal'
        
        if ball_rect.colliderect(end_rect):

            self.game.win = True
    
        
        direction, self.velocity = bounce(state, direction, self.velocity)
        direction = acvel(self.power, direction, self.velocity)[2]
        self.velocity = acvel(self.power, direction, self.velocity)[0]
        self.pos = position(self.velocity, self.pos)
        
        self.power = force(acvel(self.power, direction ,self.velocity)[1])
    
    def render(self, surf):
        surf.blit(self.image, self.rect)