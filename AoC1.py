
# read input
depths = []

with open("data/input1.txt", 'r') as f:
    for line in f:
        line = line.strip('\n')
        depths.append(int(line))

def first(depths):

    counter = 0

    for i in range(len(depths)):

        if i > 0 and depths[i] > depths[i - 1]:
            counter += 1

    return counter

def second(depths):

    # initialize
    counter = 0
    last_window_sum = 0

    for i in range(len(depths)):
        window_sum = depths[i] + depths[i-1] + depths[i-2]

        # only count when there are actual windows
        if i > 2 and window_sum > last_window_sum:
            counter += 1

        last_window_sum  = window_sum

    return counter

print(first(depths))
print(second(depths))
