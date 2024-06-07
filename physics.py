import numpy as np

f_multiplier = 0.3 

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

    pos = [x,y]
    return pos