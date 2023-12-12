import numpy as np
import itertools

filename = "input.txt"
lines = [list(line.strip()) for line in open(filename, 'r').readlines()]

def sol1():
    image = np.array(lines)
    rows_wng = np.where(np.all(image == '.', axis=1) == True)[0]
    cols_wng = np.where(np.all(image == '.', axis=0) == True)[0]
    counter = 0
    expansion = 1000000


    galaxies = np.where(image == '#')
    coords = list(zip(galaxies[0], galaxies[1]))

    pairs = list(itertools.combinations(zip(galaxies[0], galaxies[1]), 2))
    distance = 0


    for i, (c1, c2) in enumerate(pairs):
        constant = 0
        for row in rows_wng:
            if min(c1[0], c2[0]) < row < max(c1[0], c2[0]):
                constant += (expansion-1)
        
        for col in cols_wng:
            if min(c1[1], c2[1]) < col < max(c1[1], c2[1]):
                constant += (expansion-1)

        distance = distance + (abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])) + constant

    print(distance)

sol1()

