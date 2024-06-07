import numpy as np
import time
import matplotlib.pyplot as plt


f_multiplier = 0.3 
#i = 0

#velo = [0,0] #starting velocity
#posi = [0,0] #starting position
#direct = -np.pi/3   #starting direction in rads

#positx = []
#posity = []

def force(speed):
    force = -f_multiplier * speed**(1/2)
    return force

def bounce(state, direction, vel):
    velx = vel[0]
    vely = vel[1]

    if state == "horizontal":
        direction = np.pi - direction
        vely = -vely 
        
    elif state == "vertical":
        direction = (direction - np.pi)* -1
        velx = -velx
    else:
        direction = direction

    vel = [velx, vely]
    return direction, vel


def acvel(force, direction, vel):

    if direction < np.pi:
        accx = force * np.cos(direction)
        accy = force * np.sin(direction)
    else:
        accx = -force * np.cos(direction)
        accy = -force * np.sin(direction)

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

    pos = [x,y]
    return pos

"""
#purely testing purpose
while i < 30:
 
    positx.append(posi[0])
    posity.append(posi[1])


    if i == 10:
        state = "horizontal"
    else:
        state = 0
    
    direct, velo = bounce(state, direct, velo)
    
    direct = acvel(f,direct,velo)[2]

    velo = acvel(f,direct,velo)[0]
    posi = position(velo, posi)
    
    print(acvel(f,direct,velo)[1])

    f = force(acvel(f,direct,velo)[1])

    i += 1
    time.sleep(0.1)

plt.plot(positx, posity)

plt.show()

"""