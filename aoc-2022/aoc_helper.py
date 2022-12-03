### AOC HELPER FILE
import time

def read_data(filepath):
    '''
    turns raw .txt data into list of the lines
    '''
    data = []

    with open(filepath, 'r') as f:
        for line in f:
            data.append(line.strip('\n'))

    return data


def to_ints(data):
    '''
    Turns raw data into ints if input is list of ints represented as strings
    '''

    ints = []
    for line in data:
        ints.append(int(line))

    return ints

def run(input, part1, part2):

    try:
        print('Solution to part 1:')

        start = time.time()
        solution = part1(input)
        end = time.time()

        print(solution)
        print(f"this took {(end - start) * 1000} ms")
    except:
        print("There is no function for part 1 yet")

    try:
        print('\nSolution to part 2:')

        start = time.time()
        solution = part2(input)
        end = time.time()

        print(solution)
        print(f"this took {(end - start) * 1000} ms")
    except:
        print("There is no function for part 2 yet")