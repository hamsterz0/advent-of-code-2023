import re
from collections import defaultdict

filename = "input.txt"
special_characters = "/@*$=&#-+%"

def get_numbers_from_row(row):
    numbers = list()
    row = row + '.'
    start = -1
    end = -1
    for idx, val in enumerate(row):
        if start == -1 and val.isdigit():
                start = idx
        if start != -1 and not val.isdigit():
            end = idx
            number = row[start:end]
            numbers.append(number)
            start, end = -1, -1
    return numbers

def sol1():
    input = list(map(lambda x: x.strip(), open(filename, 'r').readlines()))
    sum = 0
    seen_special_chars = defaultdict(int)
    for idx, row in enumerate(input): 

        # debug purposes. 
        # for char in row:
            # seen_special_chars[char] += 1

        numbers = get_numbers_from_row(row)

        # numbers = [val for val in re.split('\.|@|\*|$|=|&|#|-|\+|%|/', row) if val and val[0].isdigit()]
        # print(len(set(numbers)) == len(numbers))
        # print(numbers)

        for number in numbers:
            lower_bound = max(0, (start := row.find(number))-1)
            upper_bound = min(len(row)-1, start + len(number))

            row = row.replace(number, '.'*len(number), 1)

            if row[lower_bound] in special_characters:
                sum += int(number)
                continue
            
            if row[upper_bound] in special_characters:
                sum += int(number)
                continue

            # search 1 lower
            if idx != len(input)-1:
                if set(special_characters).intersection(set(input[idx+1][lower_bound:upper_bound+1])):
                    sum += int(number)
                    continue

            # search 1 upper
            if idx != 0:
                if set(special_characters).intersection(set(input[idx-1][lower_bound:upper_bound+1])):
                    sum += int(number)
                    continue
            # Debug mode. 
            # print('*'*30)
            # print(idx+1, number)
            # print(input[max(0, idx-1)])
            # print(input[idx])
            # print(input[min(len(input)-1, idx+1)])
    # print(''.join([char for char in seen_special_chars.keys() if not char.isnumeric() and char != '.']))
    print(sum)

sol1()

# 303682 - too low.
# 336312 - too low. 
# 518939 - not the right answer. 
# 520019