import pygame as pg 
import sys


from createmap import MapCreator



class Main:
    def __init__(self):
        
        pg.init()
        pg.display.set_caption('ninja game')
        self.screen = pg.display.set_mode((640, 480))
        
        self.clock = pg.time.Clock()
        
        self.assets = {
            'grass' : [],
            'green' : [],
            'walls' : [],
        }
        
        #instantiate all necessary classes
        
        self.map = MapCreator(self, self.screen)
        
        
        
        self.running = True
        
        
    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
            
            
            self.map.render(self.screen)
            
        
        
Main().run()