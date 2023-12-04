## how many trees are visible from the outsides? top, bottom, right, left

import numpy as np

def read_input(input):
    '''
    returns 2d numpy array of forest with int heights of trees
    '''

    with open(input, 'r') as f:

        # initialize numpy array
        lines = [line.strip('\n') for line in f.readlines()]
        rows = len(lines[0])
        cols = len(lines)
        forest = np.zeros((cols, rows))

        for i, line in enumerate(lines):
            for j, tree in enumerate(line):
                forest[i, j] = int(tree)

    return forest

def part1(input):

    forest = read_input(input)
    size = forest.shape[0]

    visible_trees = 0

    # alle windrichtingen?
    # from left
    for i in range(size):
        treeline = forest[i, :]
        print(treeline)
        last_tree = -1
        for j, tree in enumerate(treeline):

            # if tree <= last_tree:
            
            #     continue
            
            # visible_trees += 1
            # forest[i, j] = -1
            # last_tree = tree

            if tree > last_tree:
                visible_trees += 1
                forest[i, j] = -1
                last_tree = tree

                print('current:', tree)
                print('last:', last_tree)
                print('count:', visible_trees)
            else:
                continue

    print("\nAND NOW FROM THE TOP")

    # from top
    for i in range(size):
        treeline = forest[:, i]
        print(treeline)
        last_tree = -1
        for j, tree in enumerate(treeline):

            # if tree <= last_tree:
            #     print('current:', tree)
            #     print('last:', last_tree)
            #     print('count:', visible_trees)
            #     continue
            
            # visible_trees += 1
            # forest[j, i] = -1
            # last_tree = tree

            if tree > last_tree:
                visible_trees += 1
                forest[j, i] = -1
                last_tree = tree
            else:
                continue

    print('\nAND NOW FROM THE LEFT')

    # from left
    for i in range(size):
        treeline = forest[i, :]
        print(treeline)
        last_tree = -1
        for j, tree in enumerate(np.flip(treeline)):

            # if tree <= last_tree:
            #     print('current:', tree)
            #     print('last:', last_tree)
            #     print('count:', visible_trees)
            #     continue
            
            # visible_trees += 1
            # forest[i, size-1-j] = -1
            # last_tree = tree

            if tree > last_tree:
                visible_trees += 1
                forest[i, size-1-j] = -1
                last_tree = tree
            else:
                continue

    print('\nAND NOW FROM THE BOTTOM')

    for i in range(size):
        treeline = forest[:, i]
        print(treeline)
        last_tree = -1
        for j, tree in enumerate(np.flip(treeline)):

            # if tree <= last_tree:
            #     print('current:', tree)
            #     print('last:', last_tree)
            #     print('count:', visible_trees)
            #     continue
            
            # visible_trees += 1
            # forest[size-1-j, i] = -1
            # last_tree = tree

            if tree > last_tree:
                visible_trees += 1
                forest[size-1-j, i] = -1
                last_tree = tree
            else:
                continue

    print(forest)

    return visible_trees

# read_input('inputs/8_test.txt')
print(part1('inputs/8_test.txt'))


