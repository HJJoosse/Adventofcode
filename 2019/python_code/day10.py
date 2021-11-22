import ast
import sys
import numpy as np

file_path = sys.argv[1]
with open(file_path,'r') as f:
    content = [[1 if x == "#" else 0 for x in y ] for y in f.read().split()]


asteroids = []
for y, line in enumerate(content):
    for x, pos in enumerate(line):
        if pos == 1:
            asteroids.append((x,y))

for asteroid in asteroids:
    for oth_aster in asteroids:
        if asteroid != oth_aster:
            print(np.sqrt( (asteroid[0]-oth_aster[0])**2 + (asteroid[1]-oth_aster[1])**2 ))