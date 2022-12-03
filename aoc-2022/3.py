from aoc_helper import *

def read_input(input, part=1):

    first_comps = []
    second_comps = []

    groups = []
    group = []

    with open(input, 'r') as f:

        for i, line in enumerate(f.readlines()):

            if part == 1:

                nr_items = len(line[:-1])

                first_comps.append(line[:(int(nr_items/2))])
                second_comps.append(line[(int(nr_items/2)):])

            elif part == 2:
                
                group.append(line[:-1])

                # add group + reset each 3 entries
                if (i+ 1) % 3 == 0:
                    groups.append(group)
                    group = []

    if part == 1:
        return first_comps, second_comps
    elif part == 2:
        return groups

def get_doubles(input):

    first_comps, second_comps = read_input(input)
    doubles = []

    for item1, item2 in zip(first_comps, second_comps):

        item1_set = set(item1)
        item2_set = set(item2)

        doubles.append(item1_set.intersection(item2_set).pop())

    return doubles

def get_score(doubles):

    score = 0

    for letter in doubles:

        # make use of unicode values for ordering, but just subtrackt how far the unicode value starts from the desired start
        if letter.islower():
            score += ord(letter) - 96
        else:
            score += ord(letter) - 38
    
    return score

def part1(input):

    doubles = (get_doubles(input))
    priority_sum = get_score(doubles)

    return priority_sum

def part2(input):

    groups = read_input(input, part=2)
    score = 0

    for group in groups:

        group_sets = [set(elf) for elf in group]
        common = (group_sets[0] & group_sets[1] & group_sets[2]).pop()

        if common.islower():
            score += ord(common) - 96
        else:
            score += ord(common) - 38

    return score

run('inputs/3.txt', part1, part2)