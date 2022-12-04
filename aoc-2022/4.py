from aoc_helper import *
import numpy as np

# CHANGE DAY
DAY = '4' 

def read_input(input):

    first_sections = []
    second_sections = []

    with open(input, 'r') as f:

        for pair in f.readlines():
            pair = pair.strip('\n')
            pair_split = pair.split(",")

            first = pair_split[0]
            second = pair_split[1]

            first = first.split('-')
            second = second.split('-')

            first = [int(item) for item in first]
            second = [int(item) for item in second]

            first_sections.append(first)
            second_sections.append(second)

    return first_sections, second_sections

def part1(input):

    first_sections, second_sections = read_input(input)
    dupes = 0

    # lower border = section[0], upper border = section[1]
    for section1, section2 in zip(first_sections, second_sections):

        if (int(section1[0]) >= int(section2[0]) and int(section1[1]) <= int(section2[1])) or (int(section2[0]) >= int(section1[0]) and int(section2[1]) <= int(section1[1])):
            dupes += 1

    return dupes

def part2(input):

    overlap = 0
    first_sections, second_sections = read_input(input)

    # lower border = section[0], upper border = section[1]
    for section1, section2 in zip(first_sections, second_sections):

        section1_list = np.arange(section1[0], section1[1] + 1)
        section2_list = np.arange(section2[0], section2[1] + 1)

        if len(set(section1_list) & set(section2_list)) != 0:
            overlap += 1

    return overlap

run(f'inputs/4.txt', part1, part2)
