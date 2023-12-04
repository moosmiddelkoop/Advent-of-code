
def part1(filepath):

    with open(filepath, 'r') as f:

        total = 0

        for i, line in enumerate(f.readlines()):

            card = i + 1

            # remove the first and last part
            line = line.replace(f'Card {card}: ', '')
            line = line.strip('\n')

            # split winning and own numbers
            line = line.split(' | ')

            winning_numbers = line[0].split(' ')
            our_numbers = line[1].split(' ')

            # remove empty intries in the lists
            winning_numbers = [number for number in winning_numbers if number != '']
            our_numbers = [number for number in our_numbers if number != '']

            correct = 0

            for number in our_numbers:
                if number in winning_numbers:
                    correct += 1

            score = 1 * 2 ** (correct - 1) if correct > 0 else 0
        
            total += score

    return total

def part2(filepath):

    with open(filepath, 'r') as f:

        cards_dict = {}
        winnings_dict = {}

        for i, line in enumerate(f.readlines()):

            card = i + 1

            # remove the first and last part
            line = line.replace(f'Card {card}: ', '')
            line = line.strip('\n')

            # split winning and own numbers
            line = line.split(' | ')

            winning_numbers = line[0].split(' ')
            our_numbers = line[1].split(' ')

            # remove empty intries in the lists
            winning_numbers = [number for number in winning_numbers if number != '']
            our_numbers = [number for number in our_numbers if number != '']

            # keys are ints!
            cards_dict[card] = (winning_numbers, our_numbers)

            # Now create a dict with the winnings
            correct = 0

            for number in our_numbers:
                if number in winning_numbers:
                    correct += 1

            winnings = [card + i + 1 for i in range(correct)] if correct > 0 else None

            winnings_dict[card] = winnings

    # Create a queue that doesn't dequeue
    queue = [key for key in cards_dict.keys()]

    for card in queue:
        queue.extend(winnings_dict[card]) if winnings_dict[card] != None else None

    return len(queue)

print(part2('inputs/4.txt'))