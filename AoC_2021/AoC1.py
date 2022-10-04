import aoc_helper

RAW = aoc_helper.read_data("data/input1.txt")
DATA = aoc_helper.to_ints(RAW)

def part_one(input):

    # initialize
    counter = 0

    for i in range(len(input)):

        if i > 0 and input[i] > input[i - 1]:
            counter += 1

    return counter

def part_two(input):

    # initialize
    counter = 0
    last_window_sum = 0

    for i in range(len(input)):
        window_sum = input[i] + input[i-1] + input[i-2]

        # only count when there are actual windows
        if i > 2 and window_sum > last_window_sum:
            counter += 1

        last_window_sum  = window_sum

    return counter

print(part_one(DATA))
print(part_two(DATA))
