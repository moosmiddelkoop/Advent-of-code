def read_input(input):

    opp_moves = []
    my_moves = []

    with open(input, 'r') as f:

        for line in f.readlines():

            opp_moves.append(line[0])
            my_moves.append(line[2])

    return opp_moves, my_moves

def part1(input):

    opp_moves, my_moves = read_input(input)

    # A = rock, B = paper, C = scissors
    moves_dict = {'A': {'triumphs': 'C', 'loses_to': 'B'},
                  'B': {'triumphs': 'A', 'loses_to': 'C'},
                  'C': {'triumphs': 'B', 'loses_to': 'A'}}

    translate_dict = {'X': 'A',
                      'Y': 'B',
                      'Z': 'C'}

    score = 0

    for opp_move, my_move in zip(opp_moves, my_moves):

        my_move = translate_dict[my_move]

        # shape_selected
        if my_move == 'A':
            score += 1
        elif my_move == 'B':
            score += 2
        elif my_move == 'C':
            score += 3

        # outcome
        # no need for an if statement for losing, bc then nothing happens to the point total
        if moves_dict[my_move]['triumphs'] == opp_move:
            score += 6
        elif my_move == opp_move:
            score += 3
        
    return score

def part2(input):

    opp_moves, outcomes = read_input(input)

    # A = rock, B = paper, C = scissors
    moves_dict = {'A': {'triumphs': 'C', 'loses_to': 'B'},
                  'B': {'triumphs': 'A', 'loses_to': 'C'},
                  'C': {'triumphs': 'B', 'loses_to': 'A'}}


    score = 0

    for opp_move, outcome in zip(opp_moves, outcomes):

        # i lose
        if outcome == 'X':
            my_move = moves_dict[opp_move]['triumphs']

        # we draw
        if outcome == 'Y':
            my_move = opp_move
            score += 3

        # i win
        elif outcome == 'Z':
            my_move = moves_dict[opp_move]['loses_to']
            score += 6

        # shape_selected
        if my_move == 'A':
            score += 1
        elif my_move == 'B':
            score += 2
        elif my_move == 'C':
            score += 3

    return score

print('Solution to part 1:')
print(part1('inputs/2.txt'))

print('Solution to part 2:')
print(part2('inputs/2.txt'))