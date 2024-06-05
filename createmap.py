import pygame as pg

NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

class MapCreator:
    def __init__(self, surf, tile_dim = 16):
            self.map = [open(map).readlines()[i].strip('\n') for i in range(len(open(map).readlines()))]
            self.tile_dim = tile_dim
            self.display = surf
            
            self.tilemap = []
            
            

    def tiles_nearby(self, pos): #this is necessary 
        tiles = []
        tiles_loc = (int(pos[0] // self.tile_dim), int(pos[1] // self.tile_dim))
        for near in NEIGHBOUR_OFFSETS:
            check_pos = str(pos[0] + near[0]) +  ':' + str(pos[1] + near[1])
            if check_pos in self.tile_map:
                tiles.append(self.tilemap)
        return tiles
                
    def map_tiles(self):
        pass
    
    
    
    def block_position(self):
        
        pass