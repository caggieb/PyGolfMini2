import pygame as pg
import sys

NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
NEIGHBOUR_OFFSETS = [(-1, 0), (0, -1), (1, 0),(0, 1)]
#maps/testmap.txt
PHYSICS_TILES = {'walls'}
class MapCreator:
    def __init__(self, game, surf, maps ='maps/testmap.txt' , tile_dim = 16):
            self.mapfile = [open(maps).readlines()[i].strip('\n') for i in range(len(open(maps).readlines()))]
            self.tile_dim = tile_dim
            self.display = surf
            self.game = game
            self.map = {}
            self.start = None
            self.end_rect = None
            # dictionary of dictionaries with position as the key and the type and tile variation as the value

    def tiles_nearby(self, pos): #this is necessary 
        tiles = []
        tiles_loc = (int(pos[0] // self.tile_dim), int(pos[1] // self.tile_dim))
        for near in NEIGHBOUR_OFFSETS:
            check_pos = str(int(tiles_loc[0] + near[0] + self.start[0])) +  ':' + str(int(tiles_loc[1] + near[1] + self.start[1]))
            if check_pos in self.map:
                tiles.append(self.map[check_pos])
        return tiles
                
    def map_tiles(self):
        self.rects = []
        for y, row in enumerate(self.mapfile):
            for x, tile in enumerate(row):
                loc = str(x) + ':' + str(y)
                if int(tile) == 0:
                    self.map[loc] = {'type' : 'walls', 'variant' : 0, 'pos' : [x, y]} #vertical walls
                elif int(tile) == 1:
                    self.map[loc] = {'type' : 'grass', 'variant' : 0, 'pos' : [x, y]}
                elif int(tile) == 3:
                    self.map[loc] = {'type' : 'start', 'variant' : 0, 'pos' : [x, y]}
                    self.start = (x, y)
                elif int(tile) == 2:
                    self.map[loc] = {'type' : 'flag', 'variant' : 0, 'pos' : [x, y]}
                    self.end = (x, y)
        
                    
    def rects_around(self, pos):
        rects = []
        self.end_rect = pg.Rect((self.end[0] - self.start[0]*1.25) * self.tile_dim, (self.end[0]- self.start[1]*1.25) * self.tile_dim + 32, 7, 7 )
        for tile in self.map.values():
            if tile['type'] in PHYSICS_TILES:
                rects.append(pg.Rect((tile['pos'][0] - self.start[0]*1.25) * self.tile_dim , (tile['pos'][1] - self.start[1]*1.25) * self.tile_dim, self.tile_dim, self.tile_dim))
        
        return rects, self.end_rect
                    
                    
    def render(self, surf, offset= (0, 0)):
        for x in range(int(offset[0] // self.tile_dim), int((offset[0] + surf.get_width()) // self.tile_dim + 1)):
            for y in range(int(offset[1] // self.tile_dim), int((offset[1] + surf.get_height()) // self.tile_dim + 1)):
                loc = str(x) + ':' + str(y)
                if loc in self.map:
                    tile = self.map[loc]
                    surf.blit(self.game.assets[tile['type']][tile['variant']], ((x) * self.tile_dim - offset[0], y * self.tile_dim - offset[1]))
        
         