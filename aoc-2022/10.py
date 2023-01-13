from aoc_helper import *

# CHANGE DAY
DAY = 10

def read_input(input):

    with open(input) as f:
        return [line.strip('\n') for line in f.readlines()]

def part1(input):

    instructions = read_input(input)

    cycle = 0
    X = 1
    signal_strengths = 0
    not_done_yet = [20, 60, 100, 140, 180, 220]
    
    while len(instructions) != 0:

        instruction = instructions.pop(0).split(' ')

        cycle += 1

        if cycle % 20 == 0 and cycle in not_done_yet:
            signal_strengths += (cycle * X)
            # print(cycle * X)
            not_done_yet.pop(0)

        if instruction[0] == 'addx':
            cycle += 1

            if cycle % 20 == 0 and cycle in not_done_yet:
                signal_strengths += (cycle * X)
                not_done_yet.pop(0)

            X += int(instruction[1])

    return signal_strengths

def within_three(a, b):
    diff = a - b
    return diff >= -1 and diff <= 1
        
def part2(input):

    instructions = read_input(input)
    cycle = 0
    X = 1
    output = ""

    while len(instructions) != 0:

        if cycle > 39:
            cycle %= 40
            output += '\n'

        # DRAW
        output += '#' if within_three(cycle, X) else "."
        # MOVE
        cycle += 1

        instruction = instructions.pop(0).split(' ')

        if instruction[0] == 'noop':
            continue

        if cycle > 39:
            cycle %= 40
            output += '\n'

        # DRAW
        output += '#' if within_three(cycle, X) else "."
        # MOVE
        cycle += 1
        # ADD
        X += int(instruction[1])

    return output

# run(f'inputs/{DAY}.txt', part1, part2)
print(part2('inputs/10.txt'))

