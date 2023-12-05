import re

filename = "input.txt"

def sol1():
    input = list(map(lambda x: x.strip(), open(filename, 'r').readlines()))
    sum = 0

    for idx, row in enumerate(input): 
        numbers = [val for val in re.split('\.|\*|\%|\+|\$|\@|\!', row) if val and val[0].isdigit()]

        for number in numbers:
            lower_bound = max(0, bound := row.find(number)-1)
            upper_bound = min(len(row), bound + len(number) + 2)

            # search 1 lower
            if idx != len(input)-1:
                if set('!@#$%^&*()_+').intersection(set(input[idx+1][lower_bound:upper_bound])):
                    print(number)
                    sum += int(number)
                    continue

            # search 1 upper
            if idx != 0:
                if set('!@#$%^&*()_+').intersection(set(input[idx-1][lower_bound:upper_bound])):
                    print(number)
                    sum += int(number)
                    continue
    print(sum)

sol1()