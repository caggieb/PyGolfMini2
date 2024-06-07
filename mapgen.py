import random

file_name = "maps/maze.txt"

map_width = 16
map_height = 16

start = [14,14]
end = [3,3]


midintx = start[0] - end[0]
midinty = start[1] - end[1] - 4

map_content = [""]

rnd1 = random.random()
rnd2 = random.random()

horimid = round((rnd2 * midinty)) + 4

if 0 <= rnd1 <= 0.5:
    start = [map_width - 2, map_height - 2]
    end = [3,3]

if 0.5 < rnd1 <= 1:
    start = [3, map_height - 2]
    end = [map_width - 2,3]



positions_to_update_start = [
        [start[0]-1, start[1]], [start[0]+1, start[1]],  # Left and right
        [start[0], start[1]-1], [start[0], start[1]+1],  # Top and bottom
        [start[0]-1, start[1]-1], [start[0]+1, start[1]-1],  # Top-left and top-right
        [start[0]-1, start[1]+1], [start[0]+1, start[1]+1]   # Bottom-left and bottom-right
    ]

positions_to_update_end = [
        [end[0]-1, end[1]], [end[0]+1, end[1]],  # Left and right
        [end[0], end[1]-1], [end[0], end[1]+1],  # Top and bottom
        [end[0]-1, end[1]-1], [end[0]+1, end[1]-1],  # Top-left and top-right
        [end[0]-1, end[1]+1], [end[0]+1, end[1]+1]   # Bottom-left and bottom-right
    ]

for i in range(0,map_height):
    for j in range(0,map_width):

        apply1 = False

        if i == horimid - 1 and 0 < j < map_width-1:
            apply1 = True
            map_content[i] += "1"


        if i == horimid and 0 < j < map_width-1:
            apply1 = True
            map_content[i] += "1"

        if i == horimid + 1 and 0 < j < map_width-1:
            apply1 = True
            map_content[i] += "1"
        

        if (j == start[0] or j+1 == start[0] or j+2 == start[0]) and ((start[1] < i < horimid -1 ) or (start[1]-2 > i > horimid +1)):
            apply1 = True
            map_content[i] += "1"

 
        if (j == end[0] or j+1 == end[0] or j+2 == end[0]) and ((end[1] < i < horimid -1 ) or (end[1]-2 > i > horimid +1)):
            apply1 = True
            map_content[i] += "1"           

        for k in range(len(positions_to_update_start)):
            if [j+1,i+1] == positions_to_update_start[k] or [j+1,i+1] == positions_to_update_end[k] and apply1 != True:
                apply1 = True
                map_content[i] += "1"


        if [j+1,i+1] != start and [j+1,i+1] != end and apply1 != True :
            map_content[i] += "0"
        elif [j+1,i+1] == start:
            map_content[i] += "2"
        elif [j+1,i+1] == end:
            map_content[i] += "3"
        

    map_content.append("")

map_content.remove("")

with open(file_name, "w") as file:
    for line in map_content:
        file.write(line + "\n")
        
