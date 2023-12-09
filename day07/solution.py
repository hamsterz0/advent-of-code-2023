from collections import namedtuple, Counter

Hand = namedtuple('Hand', ['cards', 'bet'])
filename = "input.txt"

def update_cards(cards):
    strength = {'A': '14', 'K': '13', 'Q': '12', 'J': '11', 'T': '10', 'J': 1}
    return list(map(lambda x: int(strength[x]) if x in strength else int(x), cards))


def handle_joker(counter):
    num_joker = counter[1]
    if num_joker == 5:
        counter['X'] = 0        # cause I need a 2^0 case to offset the score -= 1 
        return counter
    counter[1] = 0
    max_value = max(counter.values())
    most_freq_card = sorted(key for key, value in counter.items() if value == max_value)[0]
    counter[most_freq_card] += num_joker
    return counter


def sol1():
    hands = []
    with open(filename, 'r') as f:
        for line in f:
            cards, bet = line.split(' ')
            hand = Hand(update_cards(list(cards)), int(bet.strip()))
            hands.append(hand)
    
    # group them together in the the different types
    groups = [[], [], [], [], [], [], []]
    for hand in hands:
        count = Counter(hand.cards)
        score = 0
        if 1 in count.keys():
            count = handle_joker(count)
            score -= 1
        for val in count.values():
            score += pow(3, val)
        if score == 243:
            groups[0].append(hand)
        elif score == 84:
            groups[1].append(hand)
        elif score == 36:
            groups[2].append(hand)
        elif score == 33:
            groups[3].append(hand)
        elif score == 21:
            groups[4].append(hand)
        elif score == 18:
            groups[5].append(hand)
        else:
            groups[6].append(hand)
    
    print(groups[0])

    rank = 1
    score = 0
    for group in reversed(groups):
        group = sorted(group, key=lambda x: x.cards)
        # print(group)
        for hand in group:
            score += rank*hand.bet
            # print(rank, hand)
            rank += 1

    print(score)

sol1()


# 249934034 - too high
# 248836197
# 250074297


# 251417088 - your answer is too high
# 251195607