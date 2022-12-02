import pandas as pd

diagnostic = []

with open('data/input3.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        diagnostic.append(line)

df = pd.DataFrame()



def ratio(labels):

    true_amount = sum(labels)
    total_amount = len(labels)

    return true_amount / total_amount

def find_oxy(diagnostic):

    for i in range(len(diagnostic[0])):

        print(i)

        column = []

        for line in diagnostic:
            column.append(int(line[i]))

        # INT
        ratio_int = round(ratio(column))
        ratio_str = str(ratio_int)

        for line in diagnostic:

            if ratio_int == 0.5 and line[i] == 1:
                remove(line)

            elif line[i] != ratio_str:
                diagnostic.remove(line)
                print(line)
                print(len(diagnostic))

            if len(diagnostic) < 2:
                return diagnostic[0]


def find_co2(diagnostic):

    for i in range(len(diagnostic[0])):

        column = []

        for line in diagnostic:
            column.append(int(line[i]))

        # INT
        ratio_int = round(ratio(column))
        ratio_str = str(ratio_int)

        for line in diagnostic:

            if line[i] == ratio_str:
                diagnostic.remove(line)

            if len(diagnostic) == 1:
                return diagnostic[0]

def part_one(diagnostic):

    gamma = ""
    epsilon = ""

    for i in range(len(diagnostic[0])):

        column = []

        for line in diagnostic:
            column.append(int(line[i]))

        ratio_output = round(ratio(column))
        gamma += str(ratio_output)
        epsilon += str(abs(ratio_output - 1))

    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)

    return gamma_int * epsilon_int

# print(f"Part one: {part_one(diagnostic)}")

def part_two(diagnostic):

    oxy = find_oxy(diagnostic)
    co2 = find_co2(diagnostic)

    print(oxy)
    print(co2)

    oxy_int = int(oxy, 2)
    co2_int = int(co2, 2)

    return oxy_int * co2_int

# print(f"Part two: {part_two(diagnostic)}")
