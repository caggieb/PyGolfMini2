import pygame as pg 
import sys
import time

from createmap import MapCreator
from utilities import images_load
#from physics import force, bounce, acvel, position
from interface import PowerBar
from entities import Ball

class Main:
    def __init__(self):
        
        pg.init()
        pg.display.set_caption('Pygolf mini')
        self.screen = pg.display.set_mode((640, 480))
        self.display = pg.Surface((320,240))
        self.clock = pg.time.Clock()
        
        self.assets = {
            'grass' : images_load('images/grass'),
            'green' : [],
            'walls' : images_load('images/walls'),
            'empty' :0,
            'powerbar' : images_load('images/interface'),
            'start' : images_load('images/start')
        }
        #print(self.assets['walls'])
        #instantiate all necessary classes
        self.map = MapCreator(self, self.screen)
        self.map.map_tiles()
        
        self.center_offset =  (- (self.display.get_width()//2 - self.map.start[0]* self.map.tile_dim*1.25), - (self.display.get_height()//2 - self.map.start[1]* self.map.tile_dim*1.25))
        
        
        
        self.powerbar = PowerBar(self)      
        self.shoot = None
        self.ball = Ball(self)
        
        self.offset = pg.math.Vector2(self.center_offset[0], self.center_offset[1])
        self.pwr_value = 0   
        self.running = True
    
        
        
    def run(self):
        while self.running:
            start_time = time.time()
            
            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    elif event.key == pg.K_s and keys[pg.K_SPACE]:
                        self.shoot = self.pwr_value
                        self.pwr_value = 0
                    
            keys = pg.key.get_pressed()
            
            if keys[pg.K_SPACE]:
                self.pwr_value = min(self.pwr_value*1.02 + 1, 100.)
            #elif keys[pg.K_s]:
            #    self.offset.x += 1
            #    self.ball.pos[0] += 1
            #elif keys[pg.K_e]:
            #    self.offset.x -= 1
            #    self.ball.pos[0] -= 1
            self.offset[0] += self.ball.pos[0]
            self.offset[1] += self.ball.pos[1]
        
            self.pwr_value  = max(self.pwr_value  - 0.8, 0)     
            
            #self.map.
            # tiwles_nearby()
            
            self.display.fill((0, 0, 0)) 
            
            self.map.render(self.display, offset=self.offset)
            self.powerbar.custom_update()
            
            
            
            self.ball.physics(tilemap=self.map, direction=0)
            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            #provisional 
            #pg.draw.rect(self.display, (255, 255, 255), pg.Rect(0, 0, self.display.get_width(), self.display.get_height()))
            
            #self.screen.blit(self.display, (0, 0))
            self.ball.render(self.screen)
            self.powerbar.draw(self.screen)
            
            
            
            pg.display.update()
            
            elapsed_time = time.time() - start_time
            #print(f"Frame Time: {elapsed_time * 1000:.2f} ms")
            self.clock.tick(60)
Main().run()