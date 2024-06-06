import pygame as pg 
import os

def images_load(folderpath):
    images = []
    files = os.listdir(folderpath)
    for file in files:
        images.append(pg.image.load(open(folderpath + '/' + file)).convert())
    return images