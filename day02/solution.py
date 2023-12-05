import re

FILENAME = "input.txt"
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def main():
    score = 0
    with open(FILENAME, 'r') as f:
        for line in f:
            pattern = re.compile(r'(\d+)\s*([a-zA-Z]+)')
            matches = pattern.findall(line)
            impossible = False
            power = {
                'red' : 1,
                'blue': 1,
                'green': 1
            } 
            for match in matches:
                number, color = match
                number = int(number)
                # if color == 'red' and number > MAX_RED:
                #     impossible = True
                # elif color == 'green' and number > MAX_GREEN:
                #     impossible = True
                # elif color == 'blue' and number > MAX_BLUE:
                #     impossible = True

                power[color] = max(power[color], number)

            # if not impossible:
            #     score += int(line.split(':')[0].split(' ')[1])
            score += power['red'] * power['blue'] * power['green']
            

    print(score)

main()

'''
76148 - your answer is too low
76811 - your answer is too low
78669 - right answer
'''