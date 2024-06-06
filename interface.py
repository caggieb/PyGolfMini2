import pygame as pg 


class PowerBar(pg.sprite.Sprite):
    def __init__(self, group, game):
        super().__init__(group)
        self.game = game
        self.image = self.game.assets['powerbar'][0]
        
        self.display = pg.display.get_surface()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (29, 502)
        self.shoot = 0
        self.value = 0
        self.name = "pwrbar"
        self.pwr = None
        self.create_power()

    def create_power(self):
        self.pwr = pg.Rect(0, 0, 22, 98)
        self.pwr.midbottom = (29, 482)

    def custom_update(self, shoot):
        self.shoot = 0
        if shoot:
            self.shoot = self.value
            shoot = False
        # Decrease the value over time, ensure it doesn't go below 0
        self.value = max(self.value - 0.8, 0)   
        # Update the height of the power bar based on the value
        self.pwr.height = int((self.value / 100) * 98)
        self.pwr.bottomleft = (10 + 8, 512 - 128 + 98)
        
    def draw(self):
        self.display.blit(self.image, self.rect)
        pg.draw.rect(self.display, (self.value*2.55, 255-self.value*2.55, 0), self.pwr)
        for i in range(1,4):
            pg.draw.line(self.display,(82,82,81),(18,512-30-i*98/4),(28,512-30-i*98/4),3)
        for i in range(1,5):
            pg.draw.line(self.display,(82,82,81),(18,512-18-i*98/4),(23,512-18-i*98/4),2)
            
            
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
                                 
    def draw(self, surf):        
        for sprite in self.sprites():
            sprite.update()
            sprite.draw()
        
        for button in self.buttons:
            button.draw()