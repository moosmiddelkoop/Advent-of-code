from aoc_helper import *

# CHANGE DAY
DAY = 7

class Tree():
    '''
    type is either file or dir
    '''

    def __init__(self, name:str, type:str, size:int, parent:object):
        # self.children is list of tree objects
        self.children = []
        self.parent = parent
        self.name = name
        self.type = type
        self.size = size

    def add_child(self, child_name, child_type, child_size, parent):
        child = Tree(child_name, child_type, child_size, parent)
        self.children.append(child)

    def move_to(self, child_name):
        for child in self.children:
            if child.name ==  child_name:
                return child

    def calculate_size(self):
        '''
        Function to calculate size of folder. because of it's recursive nature, it immedeately also calculates
        sizes of all children
        '''

        for child in self.children:
            if child.type == 'file':
                self.size += child.size
            elif child.type == 'dir':
                self.size += child.calculate_size()

        return self.size



def read_input(input):

    # initialize tree
    System = Tree('/', 'dir', 0, None)
    MasterParent = System

    with open(input, 'r') as f:
        for line in f.readlines():

            line = line.strip('\n')
            split_line = line.split(" ")

            # dont make a move if this
            if split_line[0] == '$':
                if split_line[1] == 'ls':
                    continue

                # move to subtree if this 
                elif split_line[1] == 'cd':
                    if split_line[2] == '/':
                        System = MasterParent
                    elif split_line[2] == '..':
                        System = System.parent
                    else:
                        System = System.move_to(split_line[2])
                               
            elif split_line[0] == 'dir':
                System.add_child(split_line[1], 'dir', 0, System)
            else:
                System.add_child(split_line[1], 'file', int(split_line[0]), System)

    return MasterParent
    
def make_lists(Node, names_list, sizes_list):
    '''
    WORKS
    is recursive too
    '''

    for Child in Node.children:
        if Child.type == 'dir':
            names_list.append(Child.name)
            sizes_list.append(Child.size)
            make_lists(Child, names_list, sizes_list)

    return names_list, sizes_list

def part1(input):

    # initialize tree and calculate sizes
    MasterParent = read_input(input)
    MasterParent.calculate_size()

    # create list of folders and sizes
    names_list = [MasterParent.name]
    sizes_list = [MasterParent.size]

    names_list, sizes_list = make_lists(MasterParent, names_list, sizes_list)

    # find folders with size <= 100.000 and calculate total size of those
    total_size = sum([size for size in sizes_list if size <= 100000])

    return total_size

def part2(input):

    # initialize tree and calculate sizes
    MasterParent = read_input(input)
    MasterParent.calculate_size()

    # create list of folders and sizes
    names_list = [MasterParent.name]
    sizes_list = [MasterParent.size]

    names_list, sizes_list = make_lists(MasterParent, names_list, sizes_list)

    unused_space = 70000000 - MasterParent.size
    needed_deletion_size = 30000000 - unused_space

    sufficient_folders = [size for size in sizes_list if size >= needed_deletion_size]
    return min(sufficient_folders)
    

run(f'inputs/{DAY}.txt', part1, part2)

