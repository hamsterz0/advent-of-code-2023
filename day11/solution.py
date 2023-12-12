import numpy as np
import itertools

filename = "input.txt"
lines = [list(line.strip()) for line in open(filename, 'r').readlines()]

def sol1():
    image = np.array(lines)
    rows_wng = np.where(np.all(image == '.', axis=1) == True)
    cols_wng = np.where(np.all(image == '.', axis=0) == True)

    for row in rows_wng[0]:
        image = np.insert(image, row, ['.']*image.shape[1], axis=0)
    
    for col in cols_wng[0]:
        image = np.insert(image, col, ['.']*image.shape[0], axis=1)


    galaxies = np.where(image == '#')
    coords = list(zip(galaxies[0], galaxies[1]))
    # print(list(temp))

    pairs = list(itertools.combinations(zip(galaxies[0], galaxies[1]), 2))
    distance = 0

    for line in image.tolist():
        print(''.join(line))

    for i, (c1, c2) in enumerate(pairs):
        # if c1 == (6, 1) and c2 == (11, 6):
        #     print((abs(c1[0]-c2[0]) + abs(c1[1]-c2[1]))-1)
        distance = distance + (abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])) - 1
        # print(c1, c2, (abs(c1[0]-c2[0]) + abs(c1[1]-c2[1]))-1)
    print(distance)

    # distance = 0

    # for i in range(0, len(coords)-1):
    #     for j in range(i+1, len(coords)):
    #         galaxy1 = coords[i]
    #         galaxy2 = coords[j]

    #         print(f'Galaxy {galaxy1} and Galaxy {galaxy2} distance: {abs(galaxy1[0]-galaxy2[0]) + abs(galaxy1[1]-galaxy2[1]) - 1}')

    #         distance += abs(galaxy1[0]-galaxy2[0]) + abs(galaxy1[1]-galaxy2[1]) - 1

    # print(distance)
sol1()

