from collections import defaultdict
filename = 'input.txt'

lines = list(map(lambda x: x.strip(), open(filename, 'r').readlines()))

def sol1():
    sum = 0
    for line in lines:
        winning_cards, my_cards = line.split(' | ')
        my_cards = set(my_cards.split(' '))
        winning_cards = set(winning_cards.split(': ')[1].split(' '))

        elf_wins = winning_cards.intersection(my_cards)
        if '' in elf_wins:
            elf_wins.remove('')
        if elf_wins:
            sum += pow(2, len(elf_wins)-1)
        print(elf_wins)
    print(sum)
        

def sol2():
    sum = 0
    card_count = defaultdict(int)
    win_count = defaultdict(int)
    for idx, line in enumerate(lines):
        idx = idx+1
        winning_cards, my_cards = line.split(' | ')
        my_cards = set(my_cards.split(' '))
        winning_cards = set(winning_cards.split(': ')[1].split(' '))

        elf_wins = winning_cards.intersection(my_cards)
        card_count[idx] += 1
        if '' in elf_wins:
            elf_wins.remove('')
        if elf_wins:
            win_count[idx] = len(elf_wins)


        # 1, 2, 3, 4, 5
        for inc, _ in enumerate(elf_wins):
            card_count[idx+inc+1] += 1
    
    
    for card, count in card_count.items():
        sum += count
        increment = win_count[card]
        for inc in range(1, increment+1):
            card_count[card+inc] += (count-1)
    
    print(sum)



sol2()