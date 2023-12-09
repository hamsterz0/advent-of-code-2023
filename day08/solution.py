from collections import namedtuple, defaultdict
import math

filename = "input.txt"
Node = namedtuple("Node", ["L", "R"])

def sol1():
    graph = defaultdict(Node)

    with open(filename, 'r') as f:
        instructions = list(f.readline().strip())
        f.readline()        # getting rid of the extra line
        for line in f:
            node, children = line.strip().split(" = ")
            left, right = children.split(", ")
            left, right = left[1:], right[:-1]
            graph[node] = Node(left, right)
        
    current_node = "AAA"
    step = 0
    # print(instructions, graph)
    num_instructions = len(instructions)

    while current_node != "ZZZ":
        if instructions[step % num_instructions] == "L":
            current_node = graph[current_node].L
        else:
            current_node = graph[current_node].R
        step += 1

    print(step)


def calculate_steps(start_loc, graph, instructions):
    step = 0
    current_node = start_loc
    while current_node[-1] != 'Z':
        if instructions[step % len(instructions)] == "L":
            current_node = graph[current_node].L
        else:
            current_node = graph[current_node].R
        step += 1
    return step

def sol2():
    graph = defaultdict(Node)
    start_locations = []
    with open(filename, 'r') as f:
        instructions = list(f.readline().strip())
        f.readline()        # getting rid of the extra line
        for line in f:
            node, children = line.strip().split(" = ")
            left, right = children.split(", ")
            left, right = left[1:], right[:-1]
            graph[node] = Node(left, right)
            if node[-1] == "A":
                start_locations.append(node)

    num_steps = []
    for start_loc in start_locations:
        num_steps.append(calculate_steps(start_loc, graph, instructions))
    
    print(num_steps)
    print(math.lcm(*num_steps))

sol2()