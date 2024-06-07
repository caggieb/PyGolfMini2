import pygame as pg 


class PowerBar:
    def __init__(self, game):
        self.game = game
        self.image = pg.image.load('images/interface/pwr-bar.png')
        
        
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = (25, 475)
        
        self.pwr = pg.Rect(0, 0, 22, 98)
        self.pwr.midbottom = (25, 452)        

    def custom_update(self):

        self.pwr.height = int((self.game.pwr_value  / 100) * 98)
        self.pwr.bottomleft = (14, 485 - 128 + 98)
        
    
    def draw(self, surf):
        surf.blit(self.image, self.rect)
        pg.draw.rect(surf, (self.game.pwr_value*2.55, 255-self.game.pwr_value*2.55, 0), self.pwr)
        for i in range(1,4):
            pg.draw.line(surf,(82,82,81), (18,512-54-i*98/4), (28,512-54-i*98/4),3)
        for i in range(1,5):
            pg.draw.line(surf,(82,82,81),(18,512-40-i*98/4),(23,512-40-i*98/4),2)
            
            
class Interface(pg.sprite.Group):
    def __init__(self, game):
        super().__init__()
        self.paused = False
        self.muted = False
        self.buttons = []
        
        self.create_buttons()
        self.display = pg.display.get_surface()
    
    def create_buttons(self):
        pass
        #sound = Button(square_button_size, square_button_size, (display_w - 20, display_h - 20), text = None, color= LIGHT_GREY, hover_color=DARK_GREY)
        #pausebutton = Button(square_button_size, square_button_size, (display_w - 20,  20), '||', DARK_BEIGE, LIGHT_GREY, action= self.pause, font_size=20)
        #self.buttons.extend([sound, pausebutton])
            
    def mute_audio(self):
        self.muted = not self.muted
    
    def pause(self):
        self.paused = True
    
    def update(self):
        events = pg.event.get()
        
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.check_click(event.pos)
                                 
    def draw(self):       
        for button in self.buttons:
            button.draw()