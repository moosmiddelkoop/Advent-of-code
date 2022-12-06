from aoc_helper import *

# CHANGE DAY
DAY = 6

def part1(input):

    num_chars = 4

    with open(input, 'r') as f:
        line = f.readlines()[0]

    for i in range(len(line) - num_chars):
       
        next_4 = [char for char in line[i:i+num_chars]]
        next4_set = set(next_4)

        if len(next4_set) == num_chars:
            return i+num_chars

def part2(input):

    num_chars = 14

    with open(input, 'r') as f:
        line = f.readlines()[0]

    for i in range(len(line) - num_chars):
       
        next_4 = [char for char in line[i:i+num_chars]]
        next4_set = set(next_4)

        if len(next4_set) == num_chars:
            return i+num_chars

run(f'inputs/{DAY}.txt', part1, part2)

