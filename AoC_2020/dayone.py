numbers = set()

with open('day1.txt', 'r') as f:
    for number in f:
        numbers.add(int(number))


def look_for_numbers(numbers):
    for number1 in numbers:
        complement = 2020 - number1
        for number2 in numbers:
            number3 = complement - number2
            if number3 in numbers:
                return number1, number2, number3

n1, n2, n3 = look_for_numbers(numbers)

print(n1 * n2 * n3)
