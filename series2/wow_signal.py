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
        line = input()
        string_to_print = ''  # The string we are going to print after processing each line
        running_string = ''  # The current sequence we are working with

        for character in line:
            if character == ' ' and running_string == '':
                # If we reach a space and we have no running_string, we can simply print a dot
                string_to_print += '.'
            elif character != ' ':
                # If we reach a letter or digit, we add it to the current sequence we are working with
                running_string += character
            else:  # character == ' ' and running_string != ''
                # If we reach a space and we have a running_string, we need to check
                # if the current sequence in running_string is a WOW-Signal or not
                if not('1' in running_string or '2' in running_string or '3' in running_string or '4' in running_string) \
                        and (running_string.isdigit() or running_string.islower() or running_string.isupper()):
                    # If it is a WOW-Signal, we add the sequence to string_to_print and 1 dot for the space we reached
                    string_to_print += running_string + '.'
                else:
                    # If it is not a WOW-Signal, we replace all characters + 1 (for the space) by a dot
                    string_to_print += '.' * (len(running_string) + 1)
                    """ REMARK: Multiplication of a String means repeating the string X times """
                running_string = ''

        # There's a possibility we have a running_string at the end of our line, so we need to do the same as above
        # But then without adding an extra dot, since there was no space at the end
        if running_string != '':
            if not('1' in running_string or '2' in running_string or '3' in running_string or '4' in running_string) \
                    and (running_string.isdigit() or running_string.islower() or running_string.isupper()):
                string_to_print += running_string
            else:
                string_to_print += '.' * len(running_string)

        # Finally, print string_to_print for each line
        print(string_to_print)
    # Solution ends here


if __name__ == '__main__':
    with open('resources/input_wow_signal.txt', "r+") as file:
        lines = file.readlines()
        lines = [line.replace('\n', '') for line in lines]
    solution()
