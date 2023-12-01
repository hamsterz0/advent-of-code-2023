import string

filename = 'test_input.txt'
lines = [x.strip() for x in open(filename, 'r').readlines()]

def sol1():
    modified = list(map(lambda x: x.strip(string.ascii_letters), lines))
    print(sum([int(val[0]+val[-1]) for val in modified]))



def sol2():
    # '''
    # one
    # two
    # three
    # four
    # five
    # six
    # seven
    # eight
    # nine
    # '''
    word_mapping = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    word_list = word_mapping.keys()
    
    first_idx, last_idx = None, None
    first_number, last_number = None, None

sol2()