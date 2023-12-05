import math
from aoc_helper import *
import re

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


def part2_2(filepath):


    digit_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
                  'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',}

    with open(filepath, 'r') as f:

        total = 0
        
        for line in f.readlines():

            earliest_digit_index = math.inf
            earliest_digit = None
            latest_digit_index = -math.inf
            latest_digit = None

            for key, value in digit_dict.items():

                if line.find(key) != -1:
                    locations = [m.start() for m in re.finditer(key, line)]

                    if locations[0] < earliest_digit_index:
                        earliest_digit_index = locations[0]
                        earliest_digit = value
                    if locations[-1] > latest_digit_index:
                        latest_digit_index = locations[-1]
                        latest_digit = value

            for i, char in enumerate(line):
                
                if char.isdigit() and i < earliest_digit_index:
                    earliest_digit_index = i
                    earliest_digit = char
                if char.isdigit() and i > latest_digit_index:
                    latest_digit_index = i
                    latest_digit = char

            if earliest_digit_index == latest_digit_index:
                calibration_value = earliest_digit * 2
            else:
                calibration_value = earliest_digit + latest_digit

            total += int(calibration_value)

    return total
            

print(part2_2('inputs/1.txt'))

# run(f'inputs/{DAY}.txt', part1, part2)



