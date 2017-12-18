import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    s = 0

    #
    # TODO - implement this in part 2
    #
    
    for y in range(len(grid)):
        temp_beliefs = []
        for x in range(len(grid[0])):
           hit = (color == grid[y][x])
           temp_beliefs.append(beliefs[y][x] * (hit * p_hit + (1 - hit) * p_miss))
        new_beliefs.append(temp_beliefs)
        s = s + sum(temp_beliefs)
    #Normalization
    for y in range(len(new_beliefs)):
        for x in range(len(new_beliefs[0])):
            new_beliefs[y][x] = new_beliefs[y][x] / s
    
        
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(height)] for j in range(width)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy) % height
            new_j = (j + dx) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
