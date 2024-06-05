import numpy as np
import time

def acvel(force, direction, vel):
    accx = force * np.cos(direction)
    accy = force * np.sin(direction)

    velx = vel[0]
    vely = vel[1]

    velx += accx
    vely += accy


    direction = np.arctan2(vely, velx)

    speed = ((velx**2)+(vely**2))

    vel = [velx, vely] 
    return vel, speed, direction


def position(vel, pos):
    x = pos[0]
    y = pos[1]
    
    x += vel[0]
    y += vel[1]
    return x, y 

f = 10
velo = [0,0]
posi = [0,0]

while True:
    
    velo = acvel(f,0,velo)[0]
    posi = position(velo, posi)
    print(posi)
    print(velo)
    f = 0
    time.sleep(0.1)