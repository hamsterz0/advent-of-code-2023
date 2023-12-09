filename = "input.txt"
readings = [list(map(int, line.strip().split(' '))) for line in open(filename, 'r').readlines()]

def sol1():
    solution = 0
    for reading in readings:
        # print(reading)
        last_readings = [reading[-1]]
        first_readings = [reading[0]]
        differences = reading
        while len(set(differences)) != 1:
            differences = list(zip(differences, differences[1:]))
            differences = list(map(lambda x: x[1]-x[0], differences))
            last_readings.append(differences[-1])
            first_readings.append(differences[0])
        
        print(first_readings)
        extrapolate = 0
        for val in reversed(first_readings):
            extrapolate = val - extrapolate

        solution += extrapolate
    print(solution)

sol1()