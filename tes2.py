import random
from collections import deque

def read_maze_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    maze = [list(line) for line in lines]
    return maze

def write_maze_to_file(maze, file_name):
    with open(file_name, 'w') as file:
        for row in maze:
            file.write(''.join(row) + "\n")
    print(f"The file '{file_name}' has been updated with the generated path.")

def find_positions(maze):
    positions = {'2': None, '3': None}
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == '2':
                positions['2'] = (x, y)
            elif maze[y][x] == '3':
                positions['3'] = (x, y)
    return positions['2'], positions['3']

def is_valid(x, y, maze):
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] in {'0', '1'}

def mark_wide_path(maze, path, width=3):
    for x, y in path:
        for dx in range(-width//2, width//2 + 1):
            for dy in range(-width//2, width//2 + 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                    if maze[ny][nx] in {'0', '1'}:
                        maze[ny][nx] = '1'

def bfs(maze, start, finish):
    sx, sy = start
    fx, fy = finish
    queue = deque([(sx, sy, [(sx, sy)])])
    visited = set([(sx, sy)])
    
    while queue:
        x, y, path = queue.popleft()
        
        if (x, y) == finish:
            return path
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, maze) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path + [(nx, ny)]))
    
    return []

def create_path(file_name):
    maze = read_maze_from_file(file_name)
    start, finish = find_positions(maze)
    
    print("Maze:")
    for row in maze:
        print(''.join(row))
    
    print(f"Start position: {start}")
    print(f"Finish position: {finish}")
    
    if start is None or finish is None:
        print("Start (2) or finish (3) position not found in the maze.")
        return
    
    path = bfs(maze, start, finish)
    if path:
        print(f"Path found: {path}")
        mark_wide_path(maze, path, width=3)
    else:
        print("No path found between 2 and 3.")
    
    # Ensure start and finish remain in their positions
    sx, sy = start
    fx, fy = finish
    maze[sy][sx] = '2'
    maze[fy][fx] = '3'
    
    write_maze_to_file(maze, file_name)

# Specify the file name
file_name = "maze0.txt"

# Create the path
create_path(file_name)
