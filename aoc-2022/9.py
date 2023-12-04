from aoc_helper import *

# CHANGE DAY
DAY = 9

def tail_needs_to_move(point1, point2):
    return abs(point1[0] - point2[0]) >= 2 or abs(point1[1] - point2[1]) >= 2    

def cmp(a, b):
    return (a > b) - (a < b) 

def read_input(input):

    with open(input) as f:
        return [line.strip("\ns").split(" ") for line in f.readlines()]

def head_positions(instructions):

    starting_pos = (0,0)
    head_visited = [starting_pos]

    for instruction in instructions:
        direction = instruction[0]
        num_moves = instruction[1]

        for _ in range(int(num_moves)):
            last_position = head_visited[-1]

            if direction == 'L':
                new_position = (last_position[0] - 1, last_position[1])
                head_visited.append(new_position)

            elif direction == 'R':
                new_position = (last_position[0] + 1, last_position[1])
                head_visited.append(new_position)

            elif direction == 'U':
                new_position = (last_position[0], last_position[1] + 1)
                head_visited.append(new_position)

            elif direction == 'D':
                new_position = (last_position[0], last_position[1] - 1)
                head_visited.append(new_position)
    
    return head_visited
    

def tail_positions(head_visited):

    ## HEAD POSITIONS

    starting_pos = (0,0)
    tail_visited = [starting_pos]

    ## TAIL POSITIONS

    for head_position in head_visited:

        tail_position = tail_visited[-1]
        tail_x = tail_position[0]
        tail_y = tail_position[1]
        head_x = head_position[0]
        head_y = head_position[1]

        if tail_needs_to_move(head_position, tail_position):

            # diagonal
            if head_x != tail_x and head_y != tail_y:
                x_sign = cmp((head_x - tail_x), 0)
                y_sign = cmp((head_y - tail_y), 0)

                tail_visited.append((tail_x + x_sign, tail_y + y_sign))

            elif head_position[0] - tail_position[0] >= 2:
                tail_visited.append((tail_position[0] + 1, tail_position[1]))
            elif head_position[0] - tail_position[0] <= -2:
                tail_visited.append((tail_position[0] - 1, tail_position[1]))
            
            elif head_position[1] - tail_position[1] >= 2:
                tail_visited.append((tail_position[0], tail_position[1] + 1))
            elif head_position[1] - tail_position[1] <= -2:
                tail_visited.append((tail_position[0], tail_position[1] - 1))

    return tail_visited


def part1(input):
    
    instructions = read_input(input)
    head_visited = head_positions(instructions)
    tail_visited = tail_positions(head_visited)

    # GET NUMBER OF POSITIONS VISITED

    unique_tail_positions = set(tail_visited)

    return len(unique_tail_positions)


def part2(input):

    instructions = read_input(input)
    head_visited = head_positions(instructions)

    for i in range(9):

        tail_visited = tail_positions(head_visited)
        head_visited = tail_visited

    unique_tail_positions = set(tail_visited)
    return len(unique_tail_positions)

print(part2('inputs/9_test_2.txt'))


run(f'inputs/{DAY}.txt', part1, part2)
