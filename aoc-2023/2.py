import re
import numpy as np

def part1(filepath):
    
    possible = 0

    with open(filepath, 'r') as f:
        for i, line in enumerate(f.readlines()):

            game = i + 1

            line = line.strip('\n')
            line = line.replace(f'Game {game}: ', '')
            line = line.split(';')
            line = [subgame.split(', ') for subgame in line]
            line = [[item.strip(' ') for item in sublist] for sublist in line] 

            subgames_possible = 0

            for subgame in line:

                subgame = [item.split(' ') for item in subgame]

                # rest subgame_dict
                subgame_dict = {'blue': 0,
                            'green': 0,
                            'red': 0}    
                    
                for item in subgame:

                    subgame_dict[item[1]] += int(item[0])
           
                if subgame_dict['red'] <= 12 and subgame_dict['green'] <= 13 and subgame_dict['blue'] <= 14:
                    
                    subgames_possible += 1
                    # if we failed already, we don't have to fail another time
                
                # if all subgames are possible
                if subgames_possible == len(line):
                    possible += game

    return possible


def part2(filepath):
    
    answer = 0

    with open(filepath, 'r') as f:
        for i, line in enumerate(f.readlines()):

            game = i + 1

            line = line.strip('\n')
            line = line.replace(f'Game {game}: ', '')
            line = line.split(';')
            line = [subgame.split(', ') for subgame in line]
            line = [[item.strip(' ') for item in sublist] for sublist in line] 

            subgames_possible = 0

            most_dict = {'red': 0,
                         'green': 0,
                         'blue': 0}

            for subgame in line:

                subgame = [item.split(' ') for item in subgame]

                for item in subgame:

                    amount = int(item[0])
                    color = item[1]

                    if amount > most_dict[color]:
                        most_dict[color] = amount

            power = most_dict['red'] * most_dict['green'] * most_dict['blue']

            answer += power

    return answer


print(part2('inputs/2.txt'))