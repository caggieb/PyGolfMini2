import pygame as pg 
import os

def images_load(folderpath):
    images = []
    
    for image in folderpath:
        images.append(pg.image.load(image))
    