import re
from collections import defaultdict

filename = "input.txt"
special_characters = "/@*$=&#-+%"

input = list(map(lambda x: x.strip(), open(filename, 'r').readlines()))

gear2engines = defaultdict(list)

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
    sum = 0
    seen_special_chars = defaultdict(int)
    for idx, row in enumerate(input): 

        numbers = get_numbers_from_row(row)

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
            print(sum)


def sol2():
    sum = 0
    for idx, row in enumerate(input): 

        numbers = get_numbers_from_row(row)

        for number in numbers:
            # if number != '4' and number != '9':
            #     continue

            # this range would cover for example: .354.
            lower_bound = max(0, (start := row.find(number))-1)
            upper_bound = min(len(row)-1, start + len(number))

            row = row.replace(number, '.'*len(number), 1)

            if row[lower_bound] == '*':
                gearid = 'gear'+str(idx)+","+str(lower_bound)
                gear2engines[gearid].append(int(number))
            
            if row[upper_bound] == "*":
                gearid = 'gear'+str(idx)+","+str(upper_bound)
                gear2engines[gearid].append(int(number))
            
            if idx != 0:
                prev_row = input[idx-1]
                for loc, object in enumerate(prev_row[lower_bound:upper_bound+1]):
                    if object == "*":
                        gearid = 'gear'+str(idx-1)+","+str(loc+lower_bound)
                        gear2engines[gearid].append(int(number))
            
            if idx != len(input)-1:
                next_row = input[idx+1]
                for loc, object in enumerate(next_row[lower_bound:upper_bound+1]):
                    if object == "*":
                        gearid = 'gear'+str(idx+1)+","+str(loc+lower_bound)
                        gear2engines[gearid].append(int(number))
    
    for gearid, engines in gear2engines.items():
        if len(engines) == 2:
            sum += engines[0] * engines[1]
    
    print(gear2engines)
    print(sum)

sol2()         
# 303682 - too low.
# 336312 - too low. 
# 518939 - not the right answer. 
# 7*13 + 7*13 + 13*5 +13*15 + 4*9


# 75479712 - too low. 
# 75519888 - right answer