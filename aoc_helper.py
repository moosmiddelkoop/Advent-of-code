### AOC HELPER FILE

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

    
