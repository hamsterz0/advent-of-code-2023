import numpy as np
import sys

sys.setrecursionlimit(1000000)
np.set_printoptions(threshold=sys.maxsize)

filename = "input.txt"
lines = []

moveable_directions = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    '.': [],
    'S': [(1, 0), (0, 1), (-1, 0), (0, -1)]
}

# 1/ Works for the test cases but recursion depth reached for the final case. 

# def find_the_pipe(matrix, distance_tracker, row, col, distance):
#     if row >= matrix.shape[0] or col >= matrix.shape[1]:
#         return 
    
#     if row < 0 or col < 0:
#         return

#     if distance_tracker[row, col] <= distance:
#         return

#     if matrix[row, col] == '.':
#         return
    
#     distance_tracker[row, col] = min(distance_tracker[row, col], distance)
#     directions = moveable_directions[matrix[row, col]]
#     # visited.add((row, col))
#     new_coords = [(row+a, col+b) for a, b in directions]

#     for new_coord in new_coords:
#         # Can I even move to this new coord?
#         new_row, new_col = new_coord
#         directions = moveable_directions[matrix[new_row, new_col]]
#         valid_entry_points = [(new_row+a, new_col+b) for a, b in directions]
#         if (row, col) in valid_entry_points:
#             find_the_pipe(matrix, distance_tracker, new_row, new_col, distance+1)

#     return


def traversal_matrix(matrix, distance_tracker, prev_row, prev_col, new_row, new_col, distance):
    # base parameter checks. 
    if prev_row >= matrix.shape[0] or new_row >= matrix.shape[0]:
        return 
    
    if prev_col >= matrix.shape[1] or new_col >= matrix.shape[1]:
        return

    if prev_row < 0 or prev_col < 0 or new_row < 0 or new_col < 0:
        return
    
    if distance_tracker[new_row, new_col] <= distance:
        return 

    if matrix[new_row, new_col] == 'S':
        return 

    # Can I even come here from the previous location? 
    pipe_type = matrix[new_row, new_col]
    directions = moveable_directions[pipe_type]
    connecting_coords = [(new_row+a, new_col+b) for a, b in directions]
    if (prev_row, prev_col) not in connecting_coords:
        return 
    distance_tracker[new_row, new_col] = min(distance_tracker[new_row, new_col], distance)

    # Now where can I go next?
    connecting_coords.remove((prev_row, prev_col))
    prev_row, prev_col = new_row, new_col
    new_row, new_col = connecting_coords[0]

    return traversal_matrix(matrix, distance_tracker, prev_row, prev_col, new_row, new_col, distance+1)


def sol1():
    matrix = []
    with open(filename, 'r') as f: 
        for line in f: 
            matrix.append(list(line.strip()))

    matrix = np.array(matrix)
    distance_tracker = np.full(matrix.shape, 10000)
    start_row, start_col = np.argwhere(matrix == 'S')[0]
    distance = 0
    visited = set()

    # find_the_pipe(matrix, distance_tracker, start_row, start_col, distance)

    # trying it a slightly different way to reduce recursive calls. 
    for direction in moveable_directions[matrix[start_row, start_col]]:
        new_row, new_col = start_row + direction[0], start_col + direction[1]
        distance = 0
        traversal_matrix(matrix, distance_tracker, start_row, start_col, new_row, new_col, distance+1)

    distance_tracker[distance_tracker == 10000] = -1
    # print(distance_tracker)
    print(distance_tracker.max())



def sol2():
    pass



sol1()
sol2()