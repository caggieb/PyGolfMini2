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
        
        
    def physics(self, tilemap, direction, state = None):
        ball_rect = pg.Rect(self.pos[0] - self.image.get_width()/2, self.pos[1] - self.image.get_height()/2, self.image.get_width(), self.image.get_height())
        
        if self.game.shoot:
            self.power = (self.game.shoot**0.5)
            self.game.shoot = None   
            
        #
    
        for rect in tilemap.rects_around(self.pos):
            if ball_rect.colliderect(rect):
                if  int(self.pos[0] - self.image.get_width()) <= rect.left <= int(self.pos[0] + self.image.get_width()):
                    state = 'vertical'
                    #self.pos[0] = int(rect.left - self.image.get_width()/2)
                
                elif int(self.pos[0] + self.image.get_width()) >= rect.right >= int(self.pos[0] - self.image.get_width()):
                    #self.pos[0] = int(rect.right + self.image.get_width()/2)
                    state = 'vertical'
                    
                elif int(self.pos[1] + self.image.get_width()) >= rect.top >= int(self.pos[1] - self.image.get_width()):
                    #self.pos[1] = int(rect.top - self.image.get_width()/2)
                    state = 'horizontal'
                elif int(self.pos[1] - self.image.get_width()) <= rect.bottom <= int(self.pos[1] + self.image.get_width()):
                    #self.pos[1] = int(rect.bottom + self.image.get_width()/2)
                    state = 'horizontal'
            """    
            
            elif ball_rect.left == rect.right:
                self.pos[0] = int(rect.right + self.image.get_width()/2)
                
            elif ball_rect.top == rect.bottom:
                self.pos[1] = int(rect.bottom + self.image.get_width()/2)
            elif ball_rect.bottom == rect.top:
                self.pos[1] = int(rect.top - self.image.get_width()/2)
            """
            
    
        
        direction, self.velocity = bounce(state, direction, self.velocity)
        direction = acvel(self.power, direction, self.velocity)[2]
        self.velocity = acvel(self.power, direction, self.velocity)[0]
        self.pos = position(self.velocity, self.pos)
        #print(self.power)
        self.power = force(acvel(self.power, direction ,self.velocity)[1])
    
    def render(self, surf):
        surf.blit(self.image, self.rect)