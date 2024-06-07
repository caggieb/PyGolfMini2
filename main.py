import pygame as pg 
import sys
import time
import numpy as np

from createmap import MapCreator
from utilities import images_load
#from physics import force, bounce, acvel, position
from interface import PowerBar, Main_menu
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
            'start' : images_load('images/start'),
            'flag' : images_load('images/flag')
        }
        
        self.mainmenu = Main_menu()
        self.map = MapCreator(self, self.screen)
        self.map.map_tiles()
        self.direction = 0
        self.center_offset =  (- (self.display.get_width()//2 - self.map.start[0]* self.map.tile_dim*1.25), - (self.display.get_height()//2 - self.map.start[1]* self.map.tile_dim*1.25))
        
        self.arrow = pg.image.load('images/interface/arrow.png').convert_alpha()
        self.arrow = pg.transform.scale(self.arrow, (44, 60))
        
        
        self.win = False
        self.num = 0
        
        self.powerbar = PowerBar(self)      
        self.shoot = None
        self.ball = Ball(self)
        
        self.offset = pg.math.Vector2(0, 0)
        self.pwr_value = 0   
        self.running = True

        self.font = pg.font.Font("fonts\Pixeltype.ttf", 50)
        self.black = (0,0,0)
        
        
        
        self.win_text_surf = self.font.render('You Won!', True, (255, 0, 0))
        self.win_text_rect =  self.win_text_surf.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2))
            
    
        
        
    def run(self):
        while self.running:
            start_time = time.time()
            
            self.mainmenu.handle_events(event)
            self.mainmenu.draw()


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
                        self.num += 1
                    
           
            
            if keys[pg.K_SPACE]:
                self.pwr_value = min(self.pwr_value*1.02 + 1, 100.)
        
            elif keys[pg.K_d]:
                self.direction += 0.01
            elif keys[pg.K_a]:
                self.direction += - 0.01
                
            
            
            angle = (self.direction + np.pi) % (2 * np.pi) - np.pi
            
            self.rot_arrow = pg.transform.rotate(self.arrow, np.degrees(- angle - np.pi*0.5))
            self.rot_arrow_rect = self.rot_arrow.get_rect(center=(120, 120))
            
            text_surface = self.font.render(("Shots: " + str(self.num)), True, self.black)
            text_rect = text_surface.get_rect(topleft=(10, 10))
            
        
            self.offset[0] = int(self.ball.pos[0] + self.center_offset[0])
            self.offset[1] = int(self.ball.pos[1] + self.center_offset[1])
        
            self.pwr_value  = max(self.pwr_value  - 0.8, 0)     
            
            self.display.fill((0, 125, 178)) 
            
            self.map.render(self.display, offset=self.offset)
            self.powerbar.custom_update()
            
            
            self.ball.physics(tilemap=self.map, direction= angle)
            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            #provisional 
            
            
            
            
            self.screen.blit(self.rot_arrow, self.rot_arrow_rect)
            self.ball.render(self.screen)
            self.powerbar.draw(self.screen)
            
            
            self.screen.blit(text_surface, text_rect)
            pg.display.update()
            
            elapsed_time = time.time() - start_time
            if self.win:
                self.screen.blit(self.win_text_surf, self.win_text_rect)        
            
            #print(f"Frame Time: {elapsed_time * 1000:.2f} ms")
            self.clock.tick(60)
Main().run()