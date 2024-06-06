import pygame as pg 
import sys


from createmap import MapCreator
from utilities import images_load
from physics import force, bounce, acvel, position
from interface import Interface, PowerBar


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
            'ball'  : images_load('images/balls'),
            'powerbar' : images_load('images/interface'),
            'start' : images_load('images/start')
        }
        #print(self.assets['walls'])
        #instantiate all necessary classes
        self.map = MapCreator(self, self.screen)
        self.map.map_tiles()
        
        self.interface = Interface(self)
        PowerBar(self.interface, self)      
        
        self.offset = pg.math.Vector2(0, 0)
        
        self.running = True
        
        
    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                        
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                self.pwr_value = min(self.value*1.02 + 1, 100.)
                

            self.display.fill((0, 0, 0)) #provisional
            
            self.interface.draw(self.screen)
            self.map.render(self.display, offset=self.offset)
            
            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pg.display.update()
            self.clock.tick(60)
Main().run()