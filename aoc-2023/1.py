from aoc_helper import *

# CHANGE DAY
DAY = 1

def read_input(input):

    data = read_data(input)

    return data

def part1(input):

    data = read_input(input)
    
    total = 0
    for line in data:

        # get digits
        digits = [digit for digit in line if digit.isdigit()]

        # get addition of first and last (STRINGS) als t goed is
        added = digits[0] + digits[-1]

        # add to total
        total += int(added)

    return total

def part2(input):

    data = read_input(input)

    digit_dict = {'one': '1',
                  'two': '2',
                  'three': '3',
                  'four': '4',
                  'five': '5',
                  'six': '6',
                  'seven': '7',
                  'eight': '8',
                  'nine': '9',
                  'zero': '0'}
    
    total = 0

    data = ['gvzkmxg55twonem']

    for line in data[:1]:

        print('before replacement')
        print(line)
        found = {}

        for i in range(1, len(line) + 1):

            partial_line = line[:i]

            if line[i - 1].isdigit():
                found.append([i - 1, line[i - 1]])

            for key in digit_dict.keys():

                if key in partial_line:

                    found.append([digit_dict[key])

        print('found')
        print(found)

        # digits = [digit for digit in line if digit.isdigit()]

        # print('digits')
        # print(digits)

        # added = digits[0] + digits[-1]

        # print('added')
        # print(added)

        # total += int(added)

pass

print(part2('inputs/1.txt'))

# run(f'inputs/{DAY}.txt', part1, part2)

