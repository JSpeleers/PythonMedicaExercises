input_line_number = 0
lines = []


def input():
    global input_line_number
    input_line_number += 1
    return lines[input_line_number - 1]


def solution():
    # Solution starts here
    number_of_lines = int(input())
    for i in range(0, number_of_lines):
        full_name = input()
        # Find the location of the first space so we can differentiate first and last name
        space_index = full_name.index(" ")
        first_name = full_name[:space_index]
        last_name = full_name[space_index + 1:].replace(' ', '')  # Replace spaces by nothing == removing all spaces
        print('{}{}'.format(first_name[0].lower(), last_name[:4].lower()))
        """ REMARK: You can take a substring with an index that is larger than the string's length """
    # Solution ends here


if __name__ == '__main__':
    with open('./inputs/input_username.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    solution()
