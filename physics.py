import numpy as np
import time

f = 10 #shot power
f_multiplier = 0.02 

velo = [0,0] #starting velocity
posi = [0,0] #starting position
direct = np.pi/2   #starting direction in rads

def force(speed):
    force = -f_multiplier * speed
    return force

def bounce(state, direction):
    if state == "horizontal":
        direction = np.pi - direction
    if state == "vertical":
        direction = (direction - 2 * np.pi)* -1
    else:
        direction = direction
    return direction


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


#purely testing purpose
while abs(acvel(f,0,velo)[1]) > 0.4:
    
    velo = acvel(f,direct,velo)[0]
    posi = position(velo, posi)
    direct = bounce(0,direct)
    print(posi)
    print(acvel(f,direct,velo))

    f = force(acvel(f,direct,velo)[1])
    time.sleep(0.1)