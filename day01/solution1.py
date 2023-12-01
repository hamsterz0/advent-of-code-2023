import string

filename = 'test_input.txt'
lines = [x.strip() for x in open(filename, 'r').readlines()]

def sol1():
    modified = list(map(lambda x: x.strip(string.ascii_letters), lines))
    print(sum([int(val[0]+val[-1]) for val in modified]))



def sol2():
    word_mapping = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    word_list = word_mapping.keys()
    numbers = list('123456789')

    current_sum = 0
    
    for line in lines:
        first_idx, second_idx = 1000, -1
        first_number, second_number = None, None
        for number in numbers:
            loc1 = line.find(number)
            loc2 = line.rfind(number)
            if loc1 != -1 and (loc1 < first_idx):
                    first_idx = loc1
                    first_number = number
            if loc2 != -1 and (loc2 > second_idx):
                second_idx = loc2
                second_number = number
        
        for word in word_list:
            loc1 = line.find(word)
            loc2 = line.rfind(word)
            if loc1 != -1 and (loc1 < first_idx):
                first_idx = loc1
                first_number = word_mapping[word]
            if loc2 != -1 and (loc2 > second_idx):
                second_idx = loc2
                second_number = word_mapping[word]

        # print(first_number, second_number)
        current_sum += int(first_number + second_number)
    print(current_sum)

sol2()
