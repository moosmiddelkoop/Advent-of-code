letter_counter = 0
valid_counter = 0

with open('day2.txt', 'r') as f:
    for line in f:
        info = line.split(':')[0]
        password = line.split(':')[1]

        min_value = int(info.split('-')[0])
        max_value = int(info.split('-')[1].split(' ')[0])
        letter = info.split(' ')[1]

        for key in password:
            if key == letter:
                letter_counter += 1

        if letter_counter >= min_value and letter_counter <= max_value:
            valid_counter += 1

print(valid_counter)
