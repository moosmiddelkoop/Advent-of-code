# Advent of code day 2
# Moos Middelkoop

instructions = []

with open('data/input2.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        instructions.append(line)


def part_one(instructions):

    x = 0
    y = 0

    for instruction in instructions:

        split = instruction.split(' ')

        if split[0] == 'forward':
            x += int(split[1])
        elif split[0] == 'down':
            y += int(split[1])
        elif split[0] == 'up':
            y -= int(split[1])

    return x * y

print(f"The solution for part 1 is: {part_one(instructions)}")


def part_two(instructions):

    x = 0
    y = 0
    aim = 0

    for instruction in instructions:

        split = instruction.split(' ')

        if split[0] == 'forward':
            x += int(split[1])
            y += aim * int(split[1])
        elif split[0] == 'down':
            aim += int(split[1])
        elif split[0] == 'up':
            aim -= int(split[1])
    return x * y

print(f"The solution for part 2 is: {part_two(instructions)}")
