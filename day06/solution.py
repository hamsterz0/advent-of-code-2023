filename = "input.txt"

def sol1(race_input):

    solution = 1

    for time, distance in race_input:
        wins = 0
        for milisec in range(1, time):
            if milisec*(time - milisec) > distance:
                wins += 1
        solution *= wins
    return solution

def main():
    with open(filename, 'r') as f:
        times = list(map(int, f.readline().split(":")[1].strip().split(" ")))
        distances  = list(map(int, f.readline().split(":")[1].strip().split(" ")))
        
        race_input = zip(times, distances)

        print(sol1(race_input))

main()