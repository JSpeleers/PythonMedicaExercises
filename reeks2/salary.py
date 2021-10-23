input_line_number = 0
lines = []


def input():
    global input_line_number
    input_line_number += 1
    return lines[input_line_number - 1]


def solution():
    # Solution starts here
    total = 0
    index = 0
    first_random_number = 0

    while True:
        salary = input()
        if index == 0:
            first_random_number = int(salary)  # First number is the random number
            total = first_random_number
        elif salary == 'stop':
            break  # Stop looping when reaching final line in input
        else:
            total += int(salary)
            print('worker #{} whispers €{}'.format(index, total))
        index += 1

    print('average salary: €{:.2f}'.format((total - first_random_number) / (index - 1)))
    # Solution ends here


if __name__ == '__main__':
    with open('resources/input_salary.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    solution()
