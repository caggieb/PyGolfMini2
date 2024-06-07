import pygame as pg 
import sys

display_w = 640
display_h = 480

#list of colors used
BLACK = (0, 0, 0)
LIGHT_GREY = (153, 153, 153)
DARK_GREY = (77, 77, 77)
TURQOISE = (52, 78, 91)
BEIGE = (210, 147, 96)
BLUE = (0, 0, 255)
DARK_BEIGE = (139, 84, 39)

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
            
            
class Button: #creates a clickable and hoverable button
    def __init__(self, width, height, center_position, text, color, hover_color, action = None, font_size = 45, image = None, scale = 1):
        self.display = pg.display.get_surface()
        self.size = font_size
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pg.font.Font('fonts\Pixeltype.ttf', self.size)
        self.action = action #supposed to be some kind of function that happens when the button is clicked
        
        
        if image:
            self.image = pg.transform.scale(image, (int(image.get_width()*scale), int(image.get_height() * scale)))
            self.rect = self.image.get_rect()
        else:
            self.rect = pg.Rect(0, 0, width, height)
        
        self.rect.center = (center_position)
    
    def draw(self):
        pg.draw.rect(self.display, self.color, self.rect)
        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center = self.rect.center)
        
        self.display.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.color = self.hover_color
        else:
            self.color = LIGHT_GREY
    
    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            if self.action:
                self.action()
                
class Main_menu: #creates the main menu for starting the game
    def __init__(self):
        self.display = pg.display.get_surface()
        self.buttons = []
        self.create_buttons()
        self.started = False
        
    def create_buttons(self):
        button_width = 200
        button_height = 80
        spacing = 20
        
        Button1 = Button(button_width, button_height, (display_w//2, display_h//2 - 2 * button_height + 20), 'Start', LIGHT_GREY, DARK_GREY, action= self.start)
        Button2 = Button(button_width, button_height, (display_w//2, display_h//2), 'How to play', LIGHT_GREY, DARK_GREY, action= self.instructions)
        Button3 = Button(button_width, button_height, (display_w//2, display_h//2 + 2 * button_height - 20), 'Quit', LIGHT_GREY, DARK_GREY, action= self.quit_game)
        
        self.buttons.extend([Button1, Button2, Button3])
        
    def quit_game(self):
        pg.quit()
        sys.exit()
    
    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                    self.quit_game()
                    exit()
            elif not self.started:
                if event.type == pg.MOUSEMOTION:
                    for button in self.buttons:
                        button.check_hover(event.pos)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        button.check_click(event.pos)
        
    
    def start(self): 
        self.started = True
        print('Game has Started')
        
    
    def instructions(self):
        print('show instruction')
        
    
    def draw(self):
        self.display.fill(TURQOISE)
        for button in self.buttons:
            button.draw()