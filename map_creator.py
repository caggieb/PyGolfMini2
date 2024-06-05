import pygame as pg

NEIGHBOUR_OFFSETS = []

class MapCreator:
    def __init__(self, surf, map = 'maps\map0.txt'):
            self.map = [open(map).readlines()[i].strip('\n') for i in range(len(open(map).readlines()))]
            
            self.display = surf
            

    def create_map(self):
        tile_width, tile_height = self.grass.get_size()
        
        for y, row in enumerate(self.map):
            