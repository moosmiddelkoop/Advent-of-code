from aoc_helper import *

# CHANGE DAY
DAY = 5
NUM_CRATES = 9

def read_input(input):

    # get crate arrangement
    with open(input, 'r') as crates:

        stacks = [[] for _ in range(NUM_CRATES)]

        # get crate arrangement
        # list of lists (order is important). bc we create stacks, make sure top items are on top, so reverse at the end
        for line in crates.readlines()[:-1]:

            # 9 stacks
            for i in range(NUM_CRATES):
                crate = line[(i * 4) + 1]

                if crate != ' ':
                    stacks[i].append(crate)

        for stack in stacks:
            stack.reverse()

    return stacks


def part1(input):

    stacks = read_input(input)

    # perform instructions
    with open('inputs/5_instructions.txt', 'r') as f:
        
        for line in f.readlines():

            # parse instructions (minus one for move_from and move_to bc indexes start at 0)
            split_line = line.split(" ")
            num_crates = int(split_line[1])
            move_from = int(split_line[3]) - 1
            move_to = int(split_line[5]) - 1

            # move crate by crate
            for _ in range(num_crates):
                crate = stacks[move_from].pop(-1)
                stacks[move_to].append(crate)

    solution = ""
    for stack in stacks:
        solution += stack[-1]

    return solution

def part2(input):

    stacks = read_input(input)

    # perform instructions
    with open('inputs/5_instructions.txt', 'r') as f:
        
        for line in f.readlines():

            # parse instructions (minus one for move_from and move_to bc indexes start at 0)
            split_line = line.split(" ")
            num_crates = int(split_line[1])
            move_from = int(split_line[3]) - 1
            move_to = int(split_line[5]) - 1

            # get the crates
            in_crane = stacks[move_from][-num_crates:]
            del stacks[move_from][-num_crates:]

            # put onto new stack
            stacks[move_to] = stacks[move_to] + in_crane

    solution = ""
    for stack in stacks:
        solution += stack[-1]

    return solution

run(f'inputs/{DAY}_crates.txt', part1, part2)

