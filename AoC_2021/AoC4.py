import numpy as np

cards = []
empty_line_count = 0

with open('data/input4_test.txt', 'r') as f:
    for line in f:

        line = line.strip('\n')

        # keep track of where we are in the file
        if line == '':
            empty_line_count += 1
            continue

        # numbers first
        if empty_line_count == 0:
            numbers = line.split(",")

        # bingo cards
        else:

            # create new card if we've crossed an empty line
            if last_empty_line_count != empty_line_count:
                card = np.zeros((5, 5))
                card_line = 0

            line_split = line.split(' ')

            # problem: empty stuff
            for num in line_split.copy():
                if num == '':
                    line_split.remove(num)

            card[:, card_line] = line_split

            card_line += 1

            if last_empty_line_count != empty_line_count:
                cards.append(card)

        # update last empty line, this is used to check if the previous line
        # was an empty line
        last_empty_line_count = empty_line_count

# print(numbers)
# print(cards[:3])

# inladen is succes! nu alleen numbers nog van strings naar ints
int_map = map(int, numbers)
numbers = list(int_map)
# print(numbers)

# now the real stuff
# loop thru numbers
# use boolean array. Mask for each number, and add masks together until
# the sum of either a row or a column is 5
def part_one(cards, numbers):

    masks = []
    for i in range(len(cards)):
        masks.append(np.zeros((5, 5), dtype=bool))

    for num in numbers:
        for i, card in enumerate(cards):
            num_mask = card == num
            masks[i] = masks[i] + num_mask

            rows_sum = np.sum(masks[i], axis=1)
            cols_sum = np.sum(masks[i], axis=0)

            for row in rows_sum:
                if row == 5:
                    return card, masks[i], num
            for col in cols_sum:
                if col == 5:
                    return card, masks[i], num

winning_card, winning_card_mask, last_number = part_one(cards, numbers)

# print(winning_card)
# print(winning_card_mask)
# print(last_number)

# print(982 * last_number)


def part_two(cards, numbers):

    cards_won = []
    cards_won_amount = 0
    masks = []
    for i in range(len(cards)):
        masks.append(np.zeros((5, 5), dtype=bool))

    for num in numbers:
        for i, card in enumerate(cards):

            num_mask = card == num
            masks[i] = masks[i] + num_mask

            rows_sum = np.sum(masks[i], axis=1)
            cols_sum = np.sum(masks[i], axis=0)

            # this means we at the last card!
            if cards_won_amount == (len(cards) - 1):

                # print('hi')
                # print(cards_won)

                for row in rows_sum:
                    if i not in cards_won:
                        return card, masks[i], num
                for col in cols_sum:
                    if i not in cards_won:
                        return card, masks[i], num

            for row in rows_sum:
                if row == 5:
                    cards_won_amount += 1
                    cards_won.append(i)

                    # zodat de col ding niet ook aangeroepen wordt
                    continue

            for col in cols_sum:
                if col == 5:
                    cards_won_amount += 1
                    cards_won.append(i)


part_two(cards, numbers)

print(winning_card)
print(winning_card_mask)
print(last_number)
inverse_mask = np.logical_not(winning_card_mask)
# print(inverse_mask)
numbers_left = winning_card[inverse_mask]
print(np.sum(numbers_left) * last_number)
