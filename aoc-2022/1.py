def part1():

    with open('input_day1.txt', 'r') as f:

        elves = []
        elf = []

        for line in f.readlines():

            if line != "\n":
                elf.append(int(line))
            else:
                elves.append(elf)
                elf = []

    totals = []

    for elf in elves:
        totals.append(sum(elf))

    return totals

print("answer to part 1")
print(max(part1()))

def part2():

    totals = part1()
    totals.sort(reverse=True)

    return sum(totals[:3])

print('Answer to part 2')
print(part2())